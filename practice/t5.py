import datetime
import json
print(datetime.date.today())   # 应该出 2026-09-22
# print(date.today())            # 故意写错，看它报 NameError
today = datetime.date.today()   # ← 新增：接住，存进 today
print(today)                    # 打印出来看

text = today.isoformat()
print(text)
print(type(text))
print(text == str(today))

print(json.dumps({"date": today.isoformat()}, ensure_ascii=False))

