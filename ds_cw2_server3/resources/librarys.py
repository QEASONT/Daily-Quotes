from flask import Blueprint, render_template, Response
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from models.library import Library
from models.library_book import Book_Library
from models.book import Book
from random import choice, sample

librarys_bp = Blueprint('librarys', __name__, url_prefix='/librarys')
api = Api(librarys_bp)


@api.representation('text/html')
def output_html(data, code, headers):
    resp = Response(data)
    return resp


class LibraryAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('book_id', type=int, location='json', required=True, help='book_id is required')
        super(LibraryAPI, self).__init__()

    resource_fields = {
        'name': fields.String,
        'id': fields.Integer
    }

    
    def get(self, book_id):
        return {'Hello': 'world', 'id': book_id}

    @marshal_with(resource_fields)
    def post(self, book_id):
        parser = self.parser
        args = parser.parse_args()
        book_librarys = Book_Library.all(book_id=book_id)
        librarys = []
        for book_library in book_librarys:
            library = Library.one(id=book_library.library_id)
            librarys.append(library)
        return librarys


api.add_resource(LibraryAPI, '/<int:book_id>', endpoint='library')
