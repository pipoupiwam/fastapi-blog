import logging

from fastapi import Depends, FastAPI, status
from sqlmodel.ext.asyncio.session import AsyncSession

from . import schemas
from .database.db import get_session
from .database.services import AuthorService, ArticleService

logger = logging.getLogger("blog-logger")
app = FastAPI()


@app.on_event("startup")
async def on_startup():
    logger.info("Starting up")


# Authors
@app.get("/authors", response_model=list[schemas.Author], status_code=status.HTTP_200_OK)
async def list_authors(db: AsyncSession = Depends(get_session)):
    """
    List authors
    """
    authors = await AuthorService.list_authors(db=db)
    return authors


@app.get("/authors/{author_id}", response_model=schemas.Author, status_code=status.HTTP_200_OK)
async def delete_author(author_id: int,  db: AsyncSession = Depends(get_session)):
    author = await AuthorService.get_author(db=db, author_id=author_id)
    return author


@app.post("/authors", response_model=schemas.Author, status_code=status.HTTP_201_CREATED)
async def create_author(author: schemas.AuthorCreate, db: AsyncSession = Depends(get_session)):
    """
    Create an Author
    """
    author_instance = await AuthorService.create_author(
        db=db,
        first_name=author.first_name,
        last_name=author.last_name
    )
    return author_instance


@app.delete("/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_id: int,  db: AsyncSession = Depends(get_session)):
    await AuthorService.delete_author(db=db, author_id=author_id)


# Articles

@app.get("/articles", response_model=list[schemas.Article], status_code=status.HTTP_200_OK)
async def list_articles(db: AsyncSession = Depends(get_session)):
    """
    List Articles
    """
    articles = await ArticleService.list_articles(db=db)
    return articles


@app.get("/articles/{article_id}", response_model=schemas.Article, status_code=status.HTTP_200_OK)
async def get_author(article_id: int,  db: AsyncSession = Depends(get_session)):
    author = await ArticleService.get_article(db=db, article_id=article_id)
    return author


@app.post("/articles", response_model=schemas.Article, status_code=status.HTTP_201_CREATED)
async def create_article(article: schemas.ArticleCreate, db: AsyncSession = Depends(get_session)):
    """
    Create an article
    """
    article_instance = await ArticleService.create_article(
        db=db, title=article.title,
        content=article.title,
        author_id=article.author_id
    )
    return article_instance


@app.delete("/articles/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: int,  db: AsyncSession = Depends(get_session)):
    await ArticleService.delete_article(db=db, article_id=article_id)
