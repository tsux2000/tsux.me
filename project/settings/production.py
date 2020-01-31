"""
Django Productional Settings
"""

import os
from .base import *

# Debug
DEBUG = True

# Hosts
ALLOWED_HOSTS = ['tsux.me', 'www.tsux.me', '3.114.185.165']

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
