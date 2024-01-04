from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from . import models

import logging

logger = logging.getLogger("blog.database_services")


class ArticleService:
    """
    Service class for the Article model.
    You should implement Article related methods in this class.
    """

    @staticmethod
    async def list_articles(*, db: AsyncSession):
        result = await db.execute(select(models.Article))
        articles = result.scalars().all()
        return articles

    @staticmethod
    async def get_article(*, db: AsyncSession, article_id):
        instance = await db.get(models.Article, article_id)
        if instance is None:
            raise HTTPException(status_code=404, detail="Article does not exist")
        return instance

    @staticmethod
    async def create_article(*, db: AsyncSession, title, content, author_id):
        await AuthorService.get_author(db=db, author_id=author_id)
        article_instance = models.Article(title=title, content=content, author_id=author_id)  # type: ignore[call-arg]
        db.add(article_instance)
        await db.commit()
        await db.refresh(article_instance)
        logger.error(f"Created Article : {article_instance.title} {article_instance.content}"
                     f" {article_instance.author_id}")
        return article_instance

    @staticmethod
    async def delete_article(*, db: AsyncSession, article_id):
        instance = await ArticleService.get_article(db=db, article_id=article_id)
        logger.info(f"Deleting Article : {article_id}")
        await db.delete(instance)
        await db.commit()
        return instance

class AuthorService:
    """
    Service class for the Author model.
    You should implement Author related methods in this class
    """
    @staticmethod
    async def get_author(*, db: AsyncSession, author_id):
        instance = await db.get(models.Author, author_id)
        if instance is None:
            raise HTTPException(status_code=404, detail="Author does not exist")
        return instance

    @staticmethod
    async def list_authors(*, db: AsyncSession):
        result = await db.execute(select(models.Author))
        authors = result.scalars().all()
        return authors

    @staticmethod
    async def create_author(*, db: AsyncSession, first_name, last_name):
        author_instance = models.Author(first_name=first_name, last_name=last_name)  # type: ignore[call-arg]
        db.add(author_instance)
        await db.commit()
        await db.refresh(author_instance)
        logger.error(f"Created Author : {author_instance.first_name} {author_instance.last_name} {author_instance.id}")
        return author_instance

    @staticmethod
    async def delete_author(*, db: AsyncSession, author_id):
        instance = await AuthorService.get_author(db=db, author_id=author_id)
        logger.info(f"Deleting Author : {author_id}")
        await db.delete(instance)
        await db.commit()
        return instance
