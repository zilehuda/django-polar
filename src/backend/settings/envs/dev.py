from backend import init_logging

from ..base import *

ENV = "DEV"

CORS_ORIGIN_ALLOW_ALL = True

BASE_URL = "http://localhost/"

SECRET_KEY = "p*&=te!-z6i=mbg^jks&o8r$fbek4bj=4!9=45n!&nem4*9bv@"

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DATABASES["default"]["HOST"] = "backend_database"
DATABASES["default"]["NAME"] = "backend"
DATABASES["default"]["USER"] = "backend"
DATABASES["default"]["PASSWORD"] = "backend"
DATABASES["default"]["ENGINE"] = "django.db.backends.mysql"


INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware',)