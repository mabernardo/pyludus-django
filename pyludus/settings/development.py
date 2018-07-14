from .base import *
import os

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '83^h*jh!yj2frym(ecs@kskzvp3&0p(_44=i&4(m5xad^_%+b7'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'pyludus.sqlite3'),
    }
}

LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'celery': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
