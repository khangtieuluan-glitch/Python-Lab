def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}   # 右括号 → 它要的搭档
    stack = []

    for ch in s:
        if ch in "([{":                       # 左括号：入栈排队
            stack.append(ch)
        else:                                 # 右括号
            if not stack:                     # 栈空 = 没人在等它
                return False
            if stack.pop() != pairs[ch]:      # 栈顶必须正好是它的搭档
                return False

    return len(stack) == 0                    # 栈清空了才算全部配对
# 检测
if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("(") == False        # 抓"忘了检查栈空"
    assert is_valid("([)]") == False     # 抓"只比类型不比顺序"
    assert is_valid("") == True          # 空字符串也算合法
    print("PASS  0020_valid_parentheses")
