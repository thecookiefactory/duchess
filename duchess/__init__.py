from flask import Flask
from flask_redis import Redis

duchess = Flask(__name__)
duchess.config.from_object('config')
redis_store = Redis(duchess)

if duchess.debug:
    from flask.ext.debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(duchess)

import views
