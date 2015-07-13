import argparse
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


options = argparse.ArgumentParser()
options.add_argument('-p', '--port', dest='port', default=9500,
        type=int, help='the port to start the server on')
args = options.parse_args()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/flora/hackathon/pinchats/test.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
