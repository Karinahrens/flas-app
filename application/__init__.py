from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import *
import os

#  defining db
db = SQLAlchemy()


# Application factory

def create_app(end=None):
    app = Flask(__name__)

    #  set up the enviroment variables depending on the enviroment

    if env == 'TEST':
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["TEST_DATABASE_URL"]
    else:
        app.config['TESTING'] = False
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["TEST_DATABASE_URL"]    

# connecting db
    db.init_app(app)   

    app.app_context().push()

    CORS(app)

    from application import routes

    return app