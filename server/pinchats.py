import argparse
import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


options = argparse.ArgumentParser()
options.add_argument('-p', '--port', dest='port', default=9500,
        type=int, help='the port to start the server on')
args = options.parse_args()

# create the db engine
engine = create_engine('sqlite:////Users/flora/hackathon/pinchats/pinchats.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# use this function to initialize the db
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

def create_app():
    from routes import pinchats_blueprint
    # create the app
    app = Flask(__name__)
    app.register_blueprint(pinchats_blueprint)
    return app

if __name__ == '__main__':
    try:
        app = create_app()
        app.run(host='0.0.0.0', port=args.port)
    finally:
        db_session.remove()
