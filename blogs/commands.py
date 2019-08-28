#!/usr/bin/env python
# -*- coding:utf-8 -*-

from blogs import app
import os
import click
from faker import Faker

@app.cli.command()
@click.option('--count', default=100, help='生成虚拟数据')
def forge(count):
    click.echo('hahaha')