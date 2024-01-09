import pytest
from fastapi import status

from app.tests.fixtures import with_blog_data

pytestmark = pytest.mark.asyncio


async def test_list_authors(async_client, with_blog_data, snapshot):
    ret = await async_client.get("/articles")
    snapshot.assert_match(ret.text, "test_list_articles.json")


async def test_get_article_404(async_client, with_blog_data):
    ret = await async_client.get("/articles/404")
    assert ret.status_code == status.HTTP_404_NOT_FOUND


async def test_get_article(async_client, with_blog_data):
    ret = await async_client.get("/articles/1")
    assert ret.json()["id"] == 1
    assert ret.status_code == status.HTTP_200_OK


async def test_create_article(async_client, with_blog_data):
    ret = await async_client.post("/articles", json={
        "title": "create article",
        "content": "article content",
        "author_id": 1
    })
    ret_json = ret.json()
    assert ret_json["title"] == "create article"
    assert ret_json["content"] == "article content"
    assert ret_json["author_id"] == 1
    assert ret.status_code == status.HTTP_201_CREATED


async def test_delete_article_404(async_client, with_blog_data):
    ret = await async_client.delete("/articles/256")
    assert ret.status_code == status.HTTP_404_NOT_FOUND


async def test_delete_article(async_client, with_blog_data):
    ret = await async_client.delete("/articles/1")
    assert ret.status_code == status.HTTP_204_NO_CONTENT


