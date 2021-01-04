from backend import init_logging

from ..base import *

import os

ENV = "STAGE"


BASE_URL = "https://gany.herokuapp.com/g/"

SECRET_KEY = "p*&=te!-z6i=mbg^jks&o8r$fbek4bj=4!9=45n!&nem4*9bv@"

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DATABASES["default"]["HOST"] = os.environ.get('DATABASE_HOST', None)
DATABASES["default"]["NAME"] = os.environ.get('DATABASE_NAME', 'sqlite3.db')
DATABASES["default"]["USER"] = os.environ.get('DATABASE_USER', None)
DATABASES["default"]["PASSWORD"] = os.environ.get('DATABASE_PASSWORD', None)
DATABASES["default"]["ENGINE"] = os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3')


INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware',)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True