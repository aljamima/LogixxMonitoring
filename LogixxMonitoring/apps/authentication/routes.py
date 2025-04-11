# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us 
"""

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users

from apps.authentication.util import verify_pass

import logging
from flask import current_app, request
from datetime import datetime as dt
now = dt.now()

log_file = 'test.log'

@blueprint.route('/')
def route_default():
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting Default Route')

    return redirect(url_for('authentication_blueprint.login'))


# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting LOGIN Route')
    current_app.logger.info('Heres auth:' + str(request.authorization))

    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting Register Route')

    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting LOGOUT Route')

    logout_user()
    return redirect(url_for('authentication_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting UNAUTHORIZED Route')

    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting FORBIDDEN Route')

    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting ERROR 404 HANDLER Route')

    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    handler = logging.FileHandler(log_file)  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))
    current_app.logger.info('Starting ERROR 500 HANDLER Route')

    return render_template('home/page-500.html'), 500
