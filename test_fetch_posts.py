import pytest
from fetch_posts import fetch_posts


def test_invalid_api():
    with pytest.raises(Exception):
        fetch_posts("http://ivalid/url/", 2)


def test_api_returns_400():
    with pytest.raises(Exception) as exc_info:
        fetch_posts("https://httpbin.org/status/400")

    assert "Error fetching data from API" in str(exc_info.value)


def test_fetch_posts_returns_list():
    posts = fetch_posts("https://jsonplaceholder.typicode.com/posts")
    assert isinstance(posts, list)


def test_fetch_post_has_title_key():
    posts = fetch_posts("https://jsonplaceholder.typicode.com/posts")
    assert "title" in posts[0]


def test_fetch_posts_with_non_existing_user_id():
    posts = fetch_posts("https://jsonplaceholder.typicode.com/posts", userId=999999)
    assert isinstance(posts, list)


def test_fetch_posts_userId_filter():
    user_id = 1
    posts = fetch_posts("https://jsonplaceholder.typicode.com/posts", userId=user_id)
    for post in posts:
        assert post["userId"] == user_id
