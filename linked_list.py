# 创建节点
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# 创建链表
class LinkedList:
    def __init__(self):
        self.head = None
# 头插
    def prepend(self, value):
        self.head = Node(value, self.head)
# 尾插
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
# 删除第一个值为value的节点，如果删除成功返回True，否则返回False
    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False
# 让链表能被for循环遍历
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
# print()链表时能显示成这样
    def __repr__(self):
        return " -> ".join(str(value) for value in self) + " -> None"
# 验证代码
if __name__ == "__main__":
    ll = LinkedList()
    for x in [1, 2, 3]:
        ll.append(x)
    ll.prepend(0)
    print(ll)                  # 期望：0 -> 1 -> 2 -> 3 -> None
    print(ll.delete(2))        # 期望：True
    print(ll)                  # 期望：0 -> 1 -> 3 -> None
    print(ll.delete(99))       # 期望：False（走完全程没找到）
    print(len([x for x in ll]))  # 期望：3

            