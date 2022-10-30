import json
from tokenize import String
from flask import Blueprint, render_template, Response
from flask_restful import Api, Resource, fields, marshal_with, reqparse
import requests
from models.author import Author
from models.book import Book
from random import choice, sample

authors_bp = Blueprint('authors', __name__, url_prefix='/authors')
api = Api(authors_bp)


class AuthorAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('author_id', type=int, location='json', required=True, help='author_id is required')
        super(AuthorAPI, self).__init__()

    resource_fields = {
        'name': fields.String,
        'id': fields.Integer,
    }

    def get(self, author_id):
        return {'Hello': 'world', 'id': author_id}

    @marshal_with(resource_fields)
    def post(self, author_id):
        parser = self.parser
        args = parser.parse_args()
        books = Book.all(author_id=args['author_id'])
        return books


api.add_resource(AuthorAPI, '/<int:author_id>', endpoint='author')


class BookAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('book_name', location='json', required=True, help='book_name is required')
        super(BookAPI, self).__init__()

    resource_fields = {
        'name': fields.String,
        'id': fields.Integer,
    }

    @marshal_with(resource_fields)
    def post(self, book_name):
        parser = self.parser
        args = parser.parse_args()
        books = Book.one(name=args['book_name'])
        book_id = books.id
        CONFIG = {
            'url': 'http://127.0.0.1:5002/librarys/'+str(book_id),
            'headers': {'Content-Type': 'application/json'}
        }
        data = {'book_id': book_id}
        url = CONFIG['url']
        headers = CONFIG['headers']
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        if r.status_code != 200:
            result = r.json()
            print('Error'+str(result['message']))
            return {'Error': result}
        # print(r.json())
        return r.json()


api.add_resource(BookAPI, '/book/<string:book_name>', endpoint='book')
