"""
Django Productional Settings
"""

import os
from .base import *

# Debug
DEBUG = False

# Hosts
ALLOWED_HOSTS = []

# DB
DATABASES = {
    'default': {
        'ENGINE': '＊＊＊＊＊＊',
        'NAME': '＊＊＊＊＊＊',
        'USER': '＊＊＊＊＊＊',
        'PASSWORD': '＊＊＊＊＊＊',
        'HOST': '＊＊＊＊＊＊',
        'PORT': '＊＊＊＊＊＊',
    }
}

# Secret Key: Set with shell environment valiable
SECRET_KEY = os.environ.get('SECRET_KEY')
