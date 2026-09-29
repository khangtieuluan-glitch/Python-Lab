from linked_list import LinkedList

def make_list(values):
    """辅助函数：造一条装着 values 的链表。不是 test_ 开头，不会被当成测试跑。"""
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll

def test_append_and_repr():
    ll = make_list([1, 2, 3])
    assert str(ll) == "1 -> 2 -> 3 -> None"

def test_delete_found_returns_true():
    ll = make_list([1, 2, 3])
    assert ll.delete(2) is True
    assert str(ll) == "1 -> 3 -> None"

# 头插
def test_prepend():
        ll = make_list([1, 2, 3])
        ll.prepend(0)
        assert str(ll) == '0 -> 1 -> 2 -> 3 -> None'


# 尾插
def test_append():
        ll = make_list([1, 2, 3])
        ll.append(4)
        assert str(ll) == '1 -> 2 -> 3 -> 4 -> None'

def test_middle_empty_returns_none():
    ll = LinkedList()        # 空链表，直接造，不用 make_list
    assert ll.middle() is None
