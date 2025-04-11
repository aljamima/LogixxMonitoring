#!/usr/bin/python
# -*- encoding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from sys import exit
from decouple import config

from apps.config import config_dict
from apps import create_app, db

import logging
from flask import current_app, request
from datetime import datetime as dt
now = dt.now() 


import gunicorn


# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values

    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)


#app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, ssl_context='adhoc')
