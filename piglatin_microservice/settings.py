class Config(object):
    SECRET_KEY = "It's a secret to everybody"


class ProdConfig(Config):
    ENV = 'prod'
    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    CACHE_TYPE = 'null'


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
