import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'MY_SECREY_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/gestion_idgs804'
    SQLALCHEMY_TRACK_MODIFICATION = False
 