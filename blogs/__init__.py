#!/usr/bin/env python
# -*- coding:utf-8 -*-



import click, os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from blogs.settings import config
from blogs.blueprints.admin import admin_bp
from blogs.blueprints.auth import auth_bp
from blogs.blueprints.blog import blog_bp


app = Flask('blogs')
config_name = os.getenv('FLASK_CONFIG', 'development')
app.config.from_object(config[config_name])





app.register_blueprint(blog_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(auth_bp, url_prefix='/auth')
from blogs import commands
