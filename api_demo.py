"""api_demo.py —— 带海关的 API 脚本（A2：requests + pydantic 集成）

分工：
    requests  = 搬运工，只负责把数据搬回来
    pydantic  = 海关，负责检查数据的形状对不对

改造前：拿到 dict 直接落盘，脏数据一路混进文件；
改造后：中间插一道校验，不合规格的数据当场拦下（ValidationError）。

四块升级点：
    ① named logger   —— logger = logging.getLogger(__name__)
    ② Post(BaseModel) —— 数据契约，声明"一条帖子长什么样"
    ③ parse_posts()   —— [Post(**item) for item in raw]，批量校验
    ④ model_dump()    —— Post 对象还原成干净 dict 再序列化
"""

import json
import logging
import pathlib

import requests
from pydantic import BaseModel, ValidationError

# ① named logger：每条日志自带模块名，将来拆多文件能定位到是谁打的
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    # 多了 %(name)s —— named logger 的价值就体现在这里
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler(),
    ],
)

URL = 'https://jsonplaceholder.typicode.com/posts'


# ② 数据契约：字段、类型、必填，一次性声明清楚
class Post(BaseModel):
    """一条帖子必须长成这样。字段名要跟 API 返回的 key 完全一致。"""
    id: int
    userId: int
    title: str
    body: str


def fetch_posts(url, timeout=10):
    """requests 层：只管搬数据，不判断内容对不对。"""
    logger.info('开始请求：%s', url)
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    data = r.json()
    logger.info('请求成功，拿到 %d 条原始数据', len(data))
    return data


def parse_posts(raw):
    """pydantic 海关：list[dict] -> list[Post]

    Post(**item) 把 dict 拆成关键字参数交给 pydantic 校验：
    字段缺了、类型不对 -> 抛 ValidationError，一条都不放行。
    """
    posts = [Post(**item) for item in raw]
    logger.info('校验通过 %d 条', len(posts))
    return posts


def save_json(posts, path='data/posts.json'):
    """落盘：先把 Post 对象还原成干净 dict，再 json 序列化。"""
    data = [p.model_dump() for p in posts]
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    logger.info('已写入文件：%s（%d 条）', p, len(data))


def main():
    try:
        raw = fetch_posts(URL)
    except requests.exceptions.Timeout:
        logger.exception('请求超时')
        return
    except requests.exceptions.HTTPError as e:
        logger.error('服务器返回错误：%s', e)
        return
    except requests.exceptions.RequestException as e:
        logger.error('其他网络异常：%s', e)
        return

    try:
        posts = parse_posts(raw)
    except ValidationError as e:
        logger.error('数据校验失败，拒绝入库：%s', e.errors()[:2])
        return

    save_json(posts[:10])
    logger.info('全部完成')


if __name__ == '__main__':
    main()
