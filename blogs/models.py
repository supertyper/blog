#!/usr/bin/env python
# -*- coding:utf-8 -*-

from blogs.extensions import db
from datetime import datetime


class Admin(db.Model):
    id = db.column(db.Integer, primary_key=True)
    user_name = db.column(db.String(20))
    password_hash = db.column(db.String(128))
    blog_title = db.column(db.String(60))
    blog_sub_title = db.column(db.String(80))
    name = db.Column(db.String(30))
    about = db.column(db.Text)


class Category(db.Model):
    id = db.column(db.Integer, promary_key=True)
    name = db.column(db.String(30), unique=True)
    posts = db.relationship('Post', back_populates='category')


class Post(db.Model):
    id = db.column(db.Integer, promary_key=True)
    title = db.column(db.String(30))
    body = db.column(db.Text)
    timestamp = db.column(db.DateTime, default=datetime.now, index=True)
    category_id = db.column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='posts')
    comments = db.relationship('Comment', backref='post', cascade='all')


class Comment(db.Model):
    id = db.column(db.Integer, promary_key=True)
    author = db.column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(255))
    body = db.Column(db.Text)
    from_admin =db.Column(db.Boolean, default=False)
    reviewed = db.Column(db.Boolean, default=False)
    timestamp = db.column(db.DateTime, default=datetime.now, index=True)

    post_id = db.column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')

    replied_id = db.column(db.Integer, db.ForeignKey('comment.id'))
    replies = db.column(db.relationship('Comment'), back_populates='replied', cascade='all, delete-orphan')
    replied = db.column(db.relationship('Comment'), back_populates='replies', remote_side=[id])

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    url = db.column(db.String(255))