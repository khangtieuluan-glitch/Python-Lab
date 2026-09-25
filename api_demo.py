import pathlib
import json
import requests

URL = 'https://jsonplaceholder.typicode.com/posts'

def fetch_posts(url, timeout = 10):
    r=requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.json()

def save_json(data, path='data/posts.json'):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def main():
    try:
        posts = fetch_posts(URL)
    except requests.exceptions.Timeout:
        print('请求超时，请检查网络连接。')
        return
    except requests.exceptions.HTTPError as e:
        print(f'服务器返回错误,{e}')
        return
    except requests.exceptions.RequestException as e:
        print(f'其他异常":{e}')
        return
    save_json(posts[:10])
    print(f'前{min(10, len(posts))}条数据已保存到data/posts.json')
if __name__ == '__main__':
        main()
    

