import json
import sys

# ========== ① 先看"不接住"是什么样 ==========
# 把下面两行的注释去掉，运行一次，看完那串红字再注释回去
# print(float("abc"))
# print("这行永远不会执行")

# ========== ② 接住 ValueError：金额必须是数字 ==========
def to_amount(text):
    try:
        return float(text)
    except ValueError:
        print(f"❌ 金额必须是数字，你输入的是：{text!r}")
        return None

print("=== ② ===")
print(to_amount("25.5"))
print(to_amount("abc"))

# ========== ③ 多个 except：不同类型的错误分开处理 ==========
def load_records(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("文件还不存在，先按空列表处理")
        return []
    except json.JSONDecodeError:
        print("文件内容坏了，不是合法 JSON")
        return []

print("=== ③ ===")
print(load_records("practice/不存在的.json"))
print(load_records("practice/records.json"))

# ========== ④ IndexError：参数给少了 ==========
def get_arg(index, name):
    try:
        return sys.argv[index]
    except IndexError:
        print(f"❌ 缺少参数：{name}")
        return None

print("=== ④ ===")
print("第 1 个参数：", get_arg(1, "命令"))

# ========== ⑤ finally：无论对错都会执行 ==========
def demo_finally():
    try:
        print("正在处理…")
        1 / 0
    except ZeroDivisionError as e:
        print("接住了错误：", e)
    finally:
        print("finally：这行一定会执行")

print("=== ⑤ ===")
demo_finally()