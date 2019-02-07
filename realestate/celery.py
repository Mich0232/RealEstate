""" Celery configuration file
    requires 'tasks.py' file in app, so it can find tasks properly
    load celery app inside '__init__.py' to make sure it will run
"""
import os
from celery import Celery
from django.conf import settings

#  Default Celery settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')

#  Celery app
app = Celery('realestate')

#  load settings
app.config_from_object('django.conf:settings')
#  auto-find tasks among installed aps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
