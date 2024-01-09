import pytest
from fastapi import status

from app.tests.fixtures import with_blog_data



pytestmark = pytest.mark.asyncio


async def test_healthcheck(async_client):
    """
    Ensure that FastAPI is correctly initialized
    """
    ret = await async_client.get("/healthcheck")
    assert ret.status_code == status.HTTP_200_OK
    assert ret.json() == {"status": "ok"}


async def test_list_authors(async_client, with_blog_data, snapshot):
    ret = await async_client.get("/authors")
    snapshot.assert_match(ret.text, "test_list_authors.json")


async def test_get_author_404(async_client, with_blog_data):
    ret = await async_client.get("/authors/404")
    assert ret.status_code == status.HTTP_404_NOT_FOUND


async def test_get_author(async_client, with_blog_data):
    ret = await async_client.get("/authors/1")
    assert ret.json()["id"] == 1
    assert ret.status_code == status.HTTP_200_OK


async def test_create_author(async_client):
    ret = await async_client.post("/authors", json={
        "first_name": "create",
        "last_name": "author"
    })
    assert ret.json()["first_name"] == "create"
    assert ret.json()["last_name"] == "author"
    assert ret.status_code == status.HTTP_201_CREATED


async def test_delete_author_404(async_client, with_blog_data):
    ret = await async_client.delete("/authors/256")
    assert ret.status_code == status.HTTP_404_NOT_FOUND


async def test_delete_author(async_client, with_blog_data):
    ret = await async_client.delete("/authors/1")
    assert ret.status_code == status.HTTP_204_NO_CONTENT


