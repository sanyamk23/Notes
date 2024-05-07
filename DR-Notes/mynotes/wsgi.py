"""
WSGI config for mynotes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mynotes.settings')

application = get_wsgi_application()

SECRET_KEY = "django-insecure-fv2itn5b2aho9t#7py75u970akzlyg9hl-r7amj1(t1k0k=xj^"