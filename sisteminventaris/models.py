from flask import Flask
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy, event
from os import path
from sqlalchemy.sql.expression import desc  
from flask_login import LoginManager,UserMixin, current_user