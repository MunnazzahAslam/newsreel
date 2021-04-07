"""
WSGI config for news_reel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_reel.settings')
from whitenoise.django import DjangoWhiteNoise
  application = DjangoWhiteNoise(application)
application = get_wsgi_application()