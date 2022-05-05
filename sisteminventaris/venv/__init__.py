from flask import Flask
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy, event
from os import path
from sqlalchemy.sql.expression import desc  
from flask_login import LoginManager,UserMixin, current_user

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/pos'
    db.init_app(app)

    from .models import User

    return app