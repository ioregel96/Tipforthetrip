"""
ASGI config for tipforthetrip project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# from dotenv import load_dotenv
import os

# load_dotenv() 

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'tipforthetrip.settings.{os.getenv("ENV_STATE")}')

application = get_asgi_application()
