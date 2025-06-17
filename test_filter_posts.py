import pytest
from fetch_posts import filter_posts

posts = [
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia!! et suscipit\nsuscipit recusandae..."
    },
    {
        "userId": 2,
        "id": 2,
        "title": "sunt aut reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae..."
    }
]


def test_filter_posts_without_body():
    result = filter_posts(posts)
    expected = [
        {"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"},
        {"title": "sunt aut reprehenderit"}
    ]
    assert result == expected


def test_filter_posts_with_body():
    result = filter_posts(posts, include_body=True)
    expected = [
        {
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae..."
        },
        {
            "title": "sunt aut reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae..."
        }
    ]
    assert result == expected


def test_filter_posts_empty_list():
    result = filter_posts([])
    assert result == []
