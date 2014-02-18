import os

from flask import Flask
from flask_redis import Redis
from views import init_views


def create_app():
    duchess = Flask(__name__)
    env = os.getenv('DUCHESS_ENV', 'Development')
    duchess.config.from_object('config.%s' % env)
    redis_store = Redis(duchess)

    if duchess.debug:
        from flask.ext.debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension(duchess)

    init_views(duchess)

    return duchess
