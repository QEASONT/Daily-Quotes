
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models.base_model import db
from models.quote import Quote
from resources.author import authors_bp
# app = Flask(__name__)

# todos = {"todo2":  "build an API", "todo1": "learn Flask"}


def configured_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = configured_app()
app.register_blueprint(authors_bp, url_prefix='/authors')


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5001)
