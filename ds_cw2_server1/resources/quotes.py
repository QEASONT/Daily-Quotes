from flask import Blueprint, render_template, Response
from flask_restful import Api, Resource, fields, marshal_with
from models.quote import Quote
from models.author import Author
from models.book import Book
from random import choice, sample

quotes_bp = Blueprint('quotes', __name__, url_prefix='/quotes')
api = Api(quotes_bp)

# help with formatting the response
@api.representation('text/html')
def output_html(data, code, headers):
    resp = Response(data)
    return resp


class quote(object):
    def __init__(self, content, author):
        self.content = content
        self.author = author

# client request for a daily quote
class QuoteAPI(Resource):
    def get(self):
        quotes = Quote.all()
        au_list = []
        book_list = []
        q = sample(quotes, 10)
        for i in range(0, 10):
            au_list.append(Author.one(id=q[i].author_id))
            book_list.append(Book.one(id=q[i].book_id))
        return render_template('quotes.html', quotes=q, authors=au_list, books=book_list)


api.add_resource(QuoteAPI, '/', endpoint='quote')
