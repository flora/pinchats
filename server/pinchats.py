from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

pinchats_app = Flask(__name__)

if __name__ == '__main__':
    pinchats_app.run()
