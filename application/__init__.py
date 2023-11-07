from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import *
import os


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bxavwdqc:R7impaavOPmQMSuIF1Xbk9MJxa69a6Uw@trumpet.db.elephantsql.com/bxavwdqc" #os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

from application import routes