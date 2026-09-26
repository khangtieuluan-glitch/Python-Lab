"""CSV 读写示例（A1 收尾）

CSV 就是「用逗号分隔的纯文本表格」，比 JSON 更古老，但 Excel 直接能打开，
所以跟非程序员交换数据时特别常用。

两个必须记住的参数：
  - 写文件时 newline=''   —— 不加的话 Windows 上每行之间会多一个空行
  - 读写都加 encoding='utf-8' —— 不加的话中文在 Windows 上会乱码或直接报错
"""

import csv
import pathlib

p = pathlib.Path('data/demo.csv')
p.parent.mkdir(parents=True, exist_ok=True)   # 目录不存在就建，存在也不报错

# ---------- 写 ----------
# csv.writer 负责把列表变成一行 CSV；writerow 写一行，writerows 一次写多行
with p.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['name', 'age'])      # 表头
    w.writerow(['张三', 20])
    w.writerow(['李四', 22])
    w.writerow(['王五', 19])

print(f'已写入：{p}')

# ---------- 读 ----------
# DictReader 让每一行变成一个字典，用表头的名字取值，比记住第几列方便得多
with p.open(encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row['name'], row['age'])

# ---------- 跟 JSON 的取舍 ----------
# JSON：能存嵌套结构（列表套字典），程序之间交换数据用它
# CSV ：只能存「一行一条、列固定」的扁平表格，给人看 / 给 Excel 用选它
