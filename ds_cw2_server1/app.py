
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models.base_model import db
from models.quote import Quote
from resources.quotes import quotes_bp
from resources.author import authors_bp
from resources.book import books_bp
# app = Flask(__name__)

# todos = {"todo2":  "build an API", "todo1": "learn Flask"}


def configured_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = configured_app()
app.register_blueprint(quotes_bp, url_prefix='/quotes')
app.register_blueprint(authors_bp, url_prefix='/authors')
app.register_blueprint(books_bp, url_prefix='/books')

# api = Api(app)
# 

# class TaskListAPI(Resource):
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument('title', type=str, required=True,
#                                    help='No task title provided', location='json')
#         self.reqparse.add_argument('description', type=str, default="", location='json')
#         super(TaskListAPI, self).__init__()

#     def get(self):
#         return {'Hello': 'world'}

#     def post(seld, id):
#         return {'Hello': 'world', 'id': id}

#     # ...


# api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')


if __name__ == '__main__':
    app.run(debug=True)
