##############
### config ###
##############

import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    HASHING_METHOD = 'sha512'

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://crew-root:crew-root@localhost/crewmen'
    SQLALCHEMY_ECHO = True
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test@localhost/test?charset=utf8'
    SQLALCHEMY_ECHO = False
    DEBUG = True
