from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from routes import pinchats_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/flora/hackathon/pinchats/test.db'

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
