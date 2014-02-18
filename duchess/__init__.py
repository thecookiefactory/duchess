import os

from flask import Flask
from flask_redis import Redis
from views import init_views

duchess = Flask(__name__)
duchess.config.from_object('config.' + os.getenv('DUCHESS_ENV', 'Development'))
redis_store = Redis(duchess)

if duchess.debug:
    from flask.ext.debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(duchess)

init_views()
