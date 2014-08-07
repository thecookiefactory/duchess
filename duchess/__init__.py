import os

from flask import Flask
from flask_redis import Redis

from duchess.views import init_views
from duchess.api import api_router
from utils import autocompiler


def create_app():
    duchess = Flask(__name__, static_url_path='/static',
                    static_folder='assets')
    env = os.getenv('DUCHESS_ENV', 'Development')
    try:
        duchess.config.from_object('config.%s' % env)
    except ImportError:  # Assuming Heroku
        duchess.config.update(
            APP_DIR=os.path.abspath(os.path.dirname(__file__)),
            PROJECT_ROOT=os.path.abspath(
                os.path.join(os.path.dirname(__file__), os.pardir)
            ),
            SECRET_KEY=os.urandom(24),
            DEBUG=bool(os.getenv('DEBUG')),
            REDIS_URL=os.getenv('REDISCLOUD_URL'),
        )
    duchess.redis = Redis(duchess)

    if duchess.debug:
        from flask.ext.debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(duchess)

        autocompiler.watch_assets('duchess/assets')

    init_views(duchess)
    duchess.register_blueprint(api_router)

    return duchess
