from flask import Blueprint, render_template, Response
import json
import requests
from flask_restful import Api, Resource, fields, marshal_with
from models.author import Author
from random import choice, sample
import datetime
authors_bp = Blueprint('authors', __name__, url_prefix='/authors')
api = Api(authors_bp)


@api.representation('text/html')
def output_html(data, code, headers):
    resp = Response(data)
    return resp


# server 1 call the server 2's api to get the author information
# and then render the author information to the html page
class AuthorAPI(Resource):
    def get(self, author_id):
        CONFIG = {
            'url': 'http://127.0.0.1:5001/authors/'+str(author_id),
            'headers': {'Content-Type': 'application/json'}
        }
        data = {'author_id': author_id}
        url = CONFIG['url']
        headers = CONFIG['headers']
        starttime = datetime.datetime.now()
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        if r.status_code != 200:
            result = r.json()
            print('Error'+str(result['message']))
            return render_template('error.html', errors=result)
        endtime = datetime.datetime.now()
        print("one request time: ", (endtime - starttime).microseconds)
        print(r.json())
        author = Author.one(id=author_id)
        return render_template('books.html', author=author, books=r.json())


api.add_resource(AuthorAPI, '/<int:author_id>', endpoint='author')
