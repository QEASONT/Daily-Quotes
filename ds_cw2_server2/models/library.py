from sqlalchemy import Column, String

from models.base_model import SQLMixin, db


class Library(SQLMixin, db.Model):
    __tablename__ = 'Library'
    name = Column(String(500), nullable=False)