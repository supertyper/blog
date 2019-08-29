#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_ckeditor import CKEditor

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
ckeditor = CKEditor()