"""知识点 ⑤ datetime —— 只需 5 分钟的验证代码。

运行：python practice\\t5.py
"""

import datetime

print(datetime.date.today())                 # 2026-09-22
print(datetime.date.today().isoformat())     # 同样结果，但明确是字符串
print(type(datetime.date.today()))           # <class 'datetime.date'>
print(datetime.datetime.now())               # 带时分的完整时间
