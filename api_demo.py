import pathlib
import json
import requests
import logging

logging.basicConfig(    # ② 新增：整个程序只配这一次
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),  # 写进文件
        logging.StreamHandler(),                            # 同时打到屏幕
    ],
)

URL = 'https://jsonplaceholder.typicode.com/posts'

def fetch_posts(url, timeout = 10):
    logging.info('开始请求：%s', url)
    r=requests.get(url, timeout=timeout)
    r.raise_for_status()
    data = r.json()
    logging.info('请求成功，拿到 %d 条数据', len(data))
    return data

def save_json(data, path='data/posts.json'):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    logging.info('已写入文件：%s（%d 条）', p, len(data))
def main():
    try:
        posts = fetch_posts(URL)
    except requests.exceptions.Timeout:
        logging.exception('请求超时')
        return
    except requests.exceptions.HTTPError as e:
        logging.error('服务器返回错误：%s', e)
        return
    except requests.exceptions.RequestException as e:
        logging.error('其他网络异常：%s', e)
        return
    save_json(posts[:10])
    logging.info('全部完成')
if __name__ == '__main__':
        main()
    

