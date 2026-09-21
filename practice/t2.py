FILE = "practice/test.txt"

# 1) w = 覆盖写：文件不存在会新建，已存在会先清空
with open(FILE, "w", encoding="utf-8") as f:
    f.write("第一行：这是覆盖写入的内容\n")

# 2) a = 追加：在末尾接着写
with open(FILE, "a", encoding="utf-8") as f:
    f.write("第二行：这是追加的内容\n")

# 3) r = 读（不写就是默认读）
with open(FILE, encoding="utf-8") as f:
    content = f.read()

print("文件内容如下：")
print(content)