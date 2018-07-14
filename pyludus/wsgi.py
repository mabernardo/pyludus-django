"""
WSGI config for pyludus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.getenv('PYLUDUS_PROFILE', 'development')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyludus.settings." + env)

application = get_wsgi_application()
