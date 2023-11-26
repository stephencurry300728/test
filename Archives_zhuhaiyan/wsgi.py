"""
WSGI config for Archives_zhuhaiyan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
import django
from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError

# Set the default settings module for the 'command-line' utility.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Archives_zhuhaiyan.settings')

# Add debugging prints
print(f"Current working directory: {os.getcwd()}")

# Add automatic migration logic
django.setup()

try:
    # Attempt to connect to the database
    print("Attempting to connect to the database...")
    connections['default'].cursor()
except OperationalError:
    # If the connection fails, it may be because the database tables do not exist
    # so we run the migrations
    print("OperationalError caught, running migrations...")
    call_command('migrate')

# Get the WSGI application.
application = get_wsgi_application()
print("WSGI application has been set up.")
sys.stdout.flush()  # Ensure that print statements are flushed immediately
