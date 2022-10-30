from sqlalchemy import Column, String, Integer

from models.base_model import SQLMixin, db


class Book(SQLMixin, db.Model):
    __tablename__ = 'Book'
    name = Column(String(500), nullable=False)
    author_id = Column(Integer, nullable=False)
    # library_id = Column(Integer, nullable=False)

