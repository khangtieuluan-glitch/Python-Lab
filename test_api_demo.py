import pytest
from pydantic import ValidationError

from api_demo import Post, parse_posts


@pytest.fixture
def sample_raw():
    """三条合法的原始 dict，模拟 requests 拿回来的数据。"""
    return [
        {"id": 1, "userId": 1, "title": "a", "body": "aaa"},
        {"id": 2, "userId": 1, "title": "b", "body": "bbb"},
        {"id": 3, "userId": 2, "title": "c", "body": "ccc"},
    ]


def test_parse_posts_returns_posts(sample_raw):
    posts = parse_posts(sample_raw)
    assert len(posts) == 3
    assert all(isinstance(p, Post) for p in posts)

def test_parse_posts_keeps_fields(sample_raw):
    p = parse_posts(sample_raw)[0]
    assert p.id == 1 and p.userId == 1 and p.title == "a"

def test_parse_posts_empty_list():
    assert parse_posts([]) == []


# 宽松转换："1"、1.0 都能过海关，结果转成 int
@pytest.mark.parametrize("raw", [
    {"id": "1", "userId": "2", "title": "t", "body": "b"},
    {"id": 1.0, "userId": 2.0, "title": "t", "body": "b"},
])
def test_parse_posts_loose_types(raw):
    p = parse_posts([raw])[0]
    assert p.id == 1 and p.userId == 2


# 非法数据：必须被海关拦下
@pytest.mark.parametrize("raw", [
    {"id": 1, "title": "t", "body": "b"},                  # 缺 userId
    {"id": "abc", "userId": 1, "title": "t", "body": "b"},  # 转不成 int
    {"id": 1, "userId": None, "title": "t", "body": "b"},   # None 不放行
])
def test_parse_posts_rejects_bad(raw):
    with pytest.raises(ValidationError):
        parse_posts([raw])
