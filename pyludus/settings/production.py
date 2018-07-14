from .base import *
import os

DEBUG = False

SECRET_KEY = os.environ['PYLUDUS_SECRET_KEY']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PYLUDUS_DATABASE'],
        'USER': os.environ['PYLUDUS_USERNAME'],
        'PASSWORD': os.environ['PYLUDUS_PASSWORD'],
        'HOST': os.environ['PYLUDUS_HOST'],
        'PORT': os.getenv('PYLUDUS_PORT', '5432'),
    }
}

LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': 'ERROR',
    },
    'celery': {
        'handlers': ['console'],
        'level': 'ERROR',
    },
}
