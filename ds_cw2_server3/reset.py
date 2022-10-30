from unicodedata import name
from sqlalchemy import create_engine
import secret
from app import configured_app
from models.base_model import db
from models.quote import Quote
from models.library import Library
from models.author import Author
from models.book import Book
import json


import os
import shutil


def reset_database():
    url = 'mysql+pymysql://root:{}@localhost:3306'.format(
        secret.database_password)
    engine = create_engine(url, echo=True)

    with engine.connect() as c:
        c.execute('DROP DATABASE IF EXISTS dscw2')
        c.execute(
            'CREATE DATABASE dscw2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'
        )
        c.execute('USE dscw2')

    db.metadata.create_all(bind=engine)


def generate_book():
    lib_list = []
    au_list = []

    for i in range(0, 9):
        lib_form = dict(name='lib'+str(i))
        lib = Library.new(lib_form)
        lib_list.append(lib)

    f = open('content.json', 'r', encoding='utf-8')
    content = json.load(f)
    for i in range(0, len(content)):
        if content[i]['author'] not in au_list:
            au_form = dict(name=content[i]['author'])
            au = Author.new(au_form)
            au_list.append(content[i]['author'])

        book_form = dict(name=content[i]['title'], author_id=au.id, library_id=lib_list[i % 3].id)
        book = Book.new(book_form)
        for j in range(0, len(content[i]['paragraphs'])):
            quote_form = dict(content=content[i]['paragraphs'][j], author_id=au.id, book_id=book.id)
            quote = Quote.new(quote_form)

    f.close()




if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        reset_database()
        generate_book()
