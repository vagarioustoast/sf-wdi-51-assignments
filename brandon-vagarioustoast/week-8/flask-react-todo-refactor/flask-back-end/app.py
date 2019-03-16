import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.todos')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

DEBUG = True
PORT = 8000


@app.route('/todo', methods=['GET', 'POST'])
@app.route('/todo/<todoid>', methods=['GET', 'PUT', 'DELETE'])
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
