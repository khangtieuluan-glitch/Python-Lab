import json
import os

FILE = "practice/records.json"

# ========== ① 写：Python 对象 → 文件 ==========
records = [
    {"amount": 25.5, "note": "午饭"},
    {"amount": 8, "note": "地铁"},
]
with open(FILE, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
print("① 已写入文件：", records)

# ========== ② 读：文件 → Python 对象 ==========
with open(FILE, encoding="utf-8") as f:
    data = json.load(f)
print("② 类型是：", type(data))
print("② 内容是：", data)
print("② 第一笔备注：", data[0]["note"])


# ========== ③ 追加一笔（这就是记账脚本的 add）==========
with open(FILE, encoding="utf-8") as f:
    data = json.load(f)

data.append({"amount": 3.5, "note": "矿泉水"})

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("③ 现在共", len(data), "笔")

# ========== ④ 不碰文件，只在字符串之间转换 ==========
text = json.dumps({"a": 1, "b": "中文"}, ensure_ascii=False)
print("④ 转成字符串：", text)
obj = json.loads(text)
print("④ 转回对象后取值：", obj["b"])
# ========== ⑤ 文件不存在也不报错（第一次运行的情况）==========
if os.path.exists(FILE):
    with open(FILE, encoding="utf-8") as f:
        data = json.load(f)
else:
    data = []
print("⑤ 安全读取，共", len(data), "笔")




