import os


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.urandom(24)
    REDIS_URL = 'redis://:password@hostname:6380/0'


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
    REDIS_URL = 'redis://localhost:6379/0'
