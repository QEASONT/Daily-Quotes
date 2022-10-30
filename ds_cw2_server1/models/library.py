from sqlalchemy import Column, Integer, String

from models.base_model import SQLMixin, db


class Library(SQLMixin, db.Model):
    __tablename__ = 'Library'
    name = Column(String(50), nullable=False)
    