#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    return '<h1>hello, auth</h1>'