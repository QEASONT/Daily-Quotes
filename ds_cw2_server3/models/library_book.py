from sqlalchemy import Column, String, Integer

from models.base_model import SQLMixin, db


class Book_Library(SQLMixin, db.Model):
    __tablename__ = 'Book_Library'
    book_id = Column(Integer, nullable=False)
    library_id = Column(Integer, nullable=False)

