from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


Base = declarative_base()


def _now():
    """
    Required for freezegun to be able to freeze time properly.
    """
    return datetime.utcnow()


class TimestampMixin(object):
    created_at = mapped_column(DateTime, default=_now)
    updated_at = mapped_column(DateTime, default=_now, onupdate=_now)


class Author(TimestampMixin, Base):
    __tablename__ = 'authors'

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(25))
    last_name = mapped_column(String(25))
    articles = relationship('Article', cascade="all, delete")


class Article(TimestampMixin, Base):
    __tablename__ = 'articles'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(60))
    content = mapped_column(Text())
    author_id = mapped_column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", back_populates="articles")
