import pytest
from fastapi import HTTPException

from app.database.services import AuthorService, ArticleService
from app.tests.fixtures import with_blog_data

pytestmark = pytest.mark.asyncio


async def test_create_author(async_db, with_blog_data):
    author = await AuthorService.create_author(db=async_db, first_name="Paul", last_name="Martin")
    assert author.first_name == "Paul"
    assert author.last_name == "Martin"


async def test_get_author(async_db, with_blog_data):
    author = await AuthorService.get_author(db=async_db, author_id=1)
    assert author.first_name == "Jean"
    assert author.last_name == "Bob"


async def test_get_author_404(async_db, with_blog_data):
    with pytest.raises(HTTPException, match="404") as exc_info:
        await AuthorService.get_author(db=async_db, author_id=404)


async def test_delete_author(async_db, with_blog_data):
    await AuthorService.delete_author(db=async_db, author_id=1)
    with pytest.raises(HTTPException, match="404") as exc_info:
        await AuthorService.get_author(db=async_db, author_id=1)


async def test_delete_author_cascade_articles(async_db, with_blog_data):
    articles = await ArticleService.list_articles(db=async_db)
    assert len(articles) == 4
    await AuthorService.delete_author(db=async_db, author_id=1)
    with pytest.raises(HTTPException, match="404") as exc_info:
        await AuthorService.get_author(db=async_db, author_id=1)
    articles = await ArticleService.list_articles(db=async_db)
    assert len(articles) == 2


