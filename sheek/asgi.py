"""
ASGI config for sheek project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file_minio, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sheek.settings')

application = get_asgi_application()
