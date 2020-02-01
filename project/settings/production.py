"""
Django Productional Settings
"""

import os
from .base import *

# Debug
DEBUG = False

# Hosts
ALLOWED_HOSTS = ['tsux.me']

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_tsux',
        'USER': 'tsux',
        'PASSWORD': 'tsux',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Secret Key: Set with shell environment valiable
SECRET_KEY = os.environ.get('SECRET_KEY')
