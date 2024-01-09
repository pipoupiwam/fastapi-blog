import pytest
from fastapi import HTTPException

from app.database.services import ArticleService
from app.tests.fixtures import with_blog_data

pytestmark = pytest.mark.asyncio


async def test_create_article(async_db, with_blog_data):
    article = await ArticleService.create_article(db=async_db, title="Title", content="ZZZ", author_id=1)
    assert article.title == "Title"
    assert article.content == "ZZZ"


async def test_list_article(async_db, with_blog_data):
    article = await ArticleService.list_articles(db=async_db)
    assert len(article) == 4


async def test_get_article(async_db, with_blog_data):
    article = await ArticleService.get_article(db=async_db, article_id=1)
    assert article.title == "Article A"
    assert article.content == "AAA"


async def test_get_article_404(async_db, with_blog_data):
    with pytest.raises(HTTPException, match="404") as exc_info:
        await ArticleService.get_article(db=async_db, article_id=404)


async def test_delete_article(async_db, with_blog_data):
    await ArticleService.delete_article(db=async_db, article_id=1)
    with pytest.raises(HTTPException, match="404") as exc_info:
        await ArticleService.get_article(db=async_db, article_id=1)



