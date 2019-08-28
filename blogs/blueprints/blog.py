#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    return '<h1>hello, world!</h1>'