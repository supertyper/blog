#!/usr/bin/env python
# -*- coding:utf-8 -*-



import click, os
from flask import Flask, render_template
from blogs.settings import config
from blogs.blueprints.admin import admin_bp
from blogs.blueprints.auth import auth_bp
from blogs.blueprints.blog import blog_bp
from blogs.extensions import bootstrap, mail, db, ckeditor, moment



def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('blogs')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_logging(app)
    register_error(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    register_template_context(app)
    return app


def register_extensions(app):
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)


def register_logging(app):
    pass


def register_error(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def not_found(e):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('error/500.html'), 500


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_template_context(app):
    pass


from blogs import commands
