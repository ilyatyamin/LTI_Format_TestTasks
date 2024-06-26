"""
WSGI config for web_ltiformater project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from FormatsHandler import FormatsHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_ltiformater.settings")

application = get_wsgi_application()

manager = FormatsHandler()
