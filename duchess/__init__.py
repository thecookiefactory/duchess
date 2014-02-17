from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

duchess = Flask(__name__)
duchess.config.from_object('config')
db = SQLAlchemy(duchess)

if duchess.debug:
    from flask.ext.debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(duchess)

from duchess.views import index
