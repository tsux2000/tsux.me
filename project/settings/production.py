"""
Django Productional Settings
"""

import os
from .base import *

# Debug
DEBUG = False

# Hosts
ALLOWED_HOSTS = ['tsux.me', '3.114.198.231']

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
