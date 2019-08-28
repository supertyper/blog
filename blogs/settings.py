#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'lastflowers')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

    BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15


class Development(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:cool1994@127.0.0.1/flask_blog'

class Product(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:cool1994@127.0.0.1/flask_blog'


config = {
    'development': Development,
    'product': Product
}