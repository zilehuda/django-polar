from backend import init_logging

from ..base import *

ENV = "LOCAL"

CORS_ORIGIN_ALLOW_ALL = True

BASE_URL = "http://localhost/"

SECRET_KEY = "p*&=te!-z6i=mbg^jks&o8r$fbek4bj=4!9=45n!&nem4*9bv@"

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DATABASES["default"]["HOST"] = "django.db.backends.sqlite3"
DATABASES["default"]["NAME"] = "sqlite3.db"
DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"


# INSTALLED_APPS.append('corsheaders')
# MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware',)