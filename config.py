'''
    config.py
    Configuration module for the server
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

from uuid import uuid5, NAMESPACE_DNS
from socket import gethostname


class Config:
    def __init__(self):
        pass

    CLIENT_ID = uuid5(NAMESPACE_DNS, gethostname())
    VERSION = "1.0"
    AUTHOR = "Jake Lawrence"
    NAME = "Checkout"
    HOSTNAME = gethostname()

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    CONFIG_DIR = basedir
    LOGLEVEL = DEBUG


class ProductionConfig(Config):
    DEBUG = False
    CONFIG_DIR = '/var/log/'
    LOGLEVEL = ''

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
