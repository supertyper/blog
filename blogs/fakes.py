#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

from blogs.extensions import db
from faker import Faker
from blogs.models import Admin, Post, Category, Comment, Link
from sqlalchemy.exc import IntegrityError


fake = Faker('zh_CN')

def fake_admin():
    admin = Admin(
        user_name = '管理员',
        blog_title = '蓝色随记',
        blog_sub_title = '学习，记录，成长，改变！',
        name = 'daMao',
        about = '我是大猫，在这里，记录我的每一次改变！'
    )
    db.session.add(admin)
    db.session.commit()


def fake_category():
    category = Category(name='default')
    db.session.add(category)

    for i in range(10):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IndentationError:
            db.session.rollback()


def fake_post(count=50):
    for i in range(count):
        post = Post(
            title = fake.sentence(),
            body = fake.text(2000),
            category_id = random.randint(1, Category.query.count()),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()


def fake_links():
    weibo = Link(name='微博', url='https://weibo.com/')
    zhihu = Link(name='知乎', url='https://zhihu.com/')
    baidu = Link(name='百度', url='https://baidu.com/')
    google = Link(name='Google+', url='https://google.com/')
    db.session.add_all([weibo, zhihu, baidu, google])
    db.session.commit()