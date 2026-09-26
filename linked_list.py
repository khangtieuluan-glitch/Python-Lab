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
# 三指针链表逆转    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next      # 1. 先抓后
            current.next = prev     # 2. 再掉头
            prev = current          # 3. prev 挪
            current = nxt           # 4. current 挪（依赖第 1 步的备份）
        self.head = prev            # current 停了，prev 站在最后一个
# 快慢找中点    
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:                 # ← 只剩这一个空，你来补
            slow = slow.next           # 慢的走一步
            fast = fast.next.next      # 快的走两步
        return slow.value              # 循环停时 slow 正好站在中点
    
# Floyd 龟兔赛跑、判环
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:     # 和 middle 那行一字不差
            slow = slow.next
            fast = fast.next.next
            if slow is fast:               # ← 它俩撞上了，怎么办？
                return True
        return False                  # 能走到这儿，说明 fast 撞到了 None = 有尽头 = 没环


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

    empty = LinkedList()
    empty.reverse()
    print(empty)       # 期望：-> None（空表不崩）

    two = LinkedList()
    two.append(1)
    two.append(2)
    print(two)        # 反转前：1 -> 2 -> None
    two.reverse()
    print(two)        # 反转后：2 -> 1 -> None
    
    
    a = LinkedList()
    for x in [1, 2, 3, 4, 5]:
        a.append(x)
    print(a.middle())      # 期望：3

    b = LinkedList()
    for x in [1, 2, 3, 4]:
        b.append(x)
    print(b.middle())      # 期望：3


    c = LinkedList()
    for x in [1, 2, 3, 4]:
        c.append(x)
    node = c.head
    while node.next:          # 走到最后一个
        node = node.next
    node.next = c.head        # 让最后一个指回第一个 → 环就成了
    print(c.has_cycle())      # 期望：True

    d = LinkedList()
    for x in [1, 2, 3]:
        d.append(x)
    print(d.has_cycle())      # 期望：False




            