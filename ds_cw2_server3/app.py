
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models.base_model import db
from models.quote import Quote
from resources.librarys import librarys_bp


def configured_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = configured_app()

app.register_blueprint(librarys_bp, url_prefix='/librarys')


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5002)
