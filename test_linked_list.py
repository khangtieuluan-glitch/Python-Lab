import pytest
from linked_list import LinkedList


@pytest.fixture
def ll123():
    """每个测试都拿到一条全新的 1 -> 2 -> 3 链表。"""
    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    return ll


def make_list(values):
    """保留：给 parametrize 各不相同的输入用（不同起点不能靠 fixture）。"""
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll


def test_append_and_repr(ll123):
    assert str(ll123) == "1 -> 2 -> 3 -> None"


def test_prepend(ll123):
    ll123.prepend(0)
    assert str(ll123) == "0 -> 1 -> 2 -> 3 -> None"


def test_append(ll123):
    ll123.append(4)
    assert str(ll123) == "1 -> 2 -> 3 -> 4 -> None"


def test_middle_empty_returns_none():
    ll = LinkedList()
    assert ll.middle() is None


@pytest.mark.parametrize("values, target, expected, expected_repr", [
    ([1, 2, 3],  1,  True,  "2 -> 3 -> None"),      # 删头
    ([1, 2, 3],  2,  True,  "1 -> 3 -> None"),      # 删中间
    ([1, 2, 3],  3,  True,  "1 -> 2 -> None"),      # 删尾
    ([1, 2, 3],  99, False, "1 -> 2 -> 3 -> None"), # 删不存在
    ([],         1,  False, " -> None"),            # 空表（实现里空表 str 就是 " -> None"）
])
def test_delete_various(values, target, expected, expected_repr):
    ll = make_list(values)
    assert ll.delete(target) is expected
    assert str(ll) == expected_repr
