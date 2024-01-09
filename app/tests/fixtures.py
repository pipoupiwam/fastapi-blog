import pytest_asyncio

from app.database.services import AuthorService, ArticleService
from conftest import async_db


@pytest_asyncio.fixture
async def with_blog_data(async_db):
    jean_author = await AuthorService.create_author(db=async_db, first_name="Jean", last_name="Bob")
    await ArticleService.create_article(db=async_db, author_id=jean_author.id, title="Article A", content="AAA")
    await ArticleService.create_article(db=async_db, author_id=jean_author.id, title="Article B", content="BBB")
    martin_author = await AuthorService.create_author(db=async_db, first_name="Martin", last_name="Luc")
    await ArticleService.create_article(db=async_db, author_id=martin_author.id, title="Article C", content="CCC")
    await ArticleService.create_article(db=async_db, author_id=martin_author.id, title="Article D", content="DDD")

