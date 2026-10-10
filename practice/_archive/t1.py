import sys

print("收到的全部内容", sys.argv)
print("第一个参数", sys.argv[1] if len(sys.argv) > 1 else "没传")