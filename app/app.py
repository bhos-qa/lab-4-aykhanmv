# app.py
from flask import Flask
import os
from dotenv import load_dotenv
from models import db
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university_pms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from controllers import *
from models import *

if __name__ == '__main__':
    app.init_app(db)
    app.run(debug=True)

