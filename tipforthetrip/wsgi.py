"""
WSGI config for tipforthetrip project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

# from dotenv import load_dotenv
# load_dotenv() 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'tipforthetrip.settings.{os.getenv("ENV_STATE")}')

application = get_wsgi_application()