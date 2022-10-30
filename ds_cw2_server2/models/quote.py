import time

from sqlalchemy import Column, Unicode, UnicodeText, Integer

from models.base_model import SQLMixin, db


class Quote(SQLMixin, db.Model):
    content = Column(UnicodeText, nullable=False)
    author_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
 
