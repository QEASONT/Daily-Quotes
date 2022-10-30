from dbm.ndbm import library
from flask import Blueprint, Response, render_template
import requests
import json
from flask_restful import Api, Resource, fields, marshal_with
from models.book import Book
from random import choice
import datetime
from models.library_book import Book_Library

books_bp = Blueprint('books', __name__, url_prefix='/books')
api = Api(books_bp)


@api.representation('text/html')
def output_html(data, code, headers):
    resp = Response(data)
    return resp

# server 1 call the server 2's api to get the book information
# and then render the book information to the html page


class BookAPI(Resource):
    def get(self, book_name):
        book = Book.one(name=book_name)

        CONFIG = {
            'url': 'http://127.0.0.1:5001/authors/book/'+str(book_name),
            'headers': {'Content-Type': 'application/json'}
        }
        data = {'book_name': book_name}
        url = CONFIG['url']
        headers = CONFIG['headers']
        starttime = datetime.datetime.now()
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        if r.status_code != 200:
            result = r.json()
            print('Error'+str(result['message']))
            return render_template('error.html', errors=result)
        endtime = datetime.datetime.now()
        print("two request time: ", (endtime - starttime).microseconds)
        print(r.json())
        return render_template('librarys.html', book=book, librarys=r.json())


api.add_resource(BookAPI, '/<string:book_name>', endpoint='book')
