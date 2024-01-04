from datetime import datetime

from pydantic import BaseModel
import logging

logger = logging.getLogger("blog-logger.services")

# Article Model

class ArticleBase(BaseModel):
    title: str
    content: str
    author_id: int


class ArticleCreate(ArticleBase):
    """
    Pydantic model to create Article instance
    """
    pass


class Article(ArticleBase):
    """
    Database model for Article table
    """
    id: int

    class Config:
        orm_mode = True



# Writer Model
class AuthorBase(BaseModel):
    first_name: str
    last_name: str


class AuthorCreate(AuthorBase):
    """
    Pydantic model to create Author instance
    """
    pass


class Author(AuthorBase):
    """
    Database model for Author table
    """
    id: int
    created_at: datetime
    updated_at: datetime


    class Config:
        orm_mode = True

