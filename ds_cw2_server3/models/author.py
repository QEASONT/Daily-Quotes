from sqlalchemy import Column, String

from models.base_model import SQLMixin, db


class Author(SQLMixin, db.Model):
    __tablename__ = 'Author'
    name = Column(String(500), nullable=False)