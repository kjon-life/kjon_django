#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    """LOCAL"""
    # Set default settings module for the 'manage.py' command-line utility before loading .env file.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kjon_django.settings')

    # Load the .env file
    dotenv_path = os.path.expanduser('.env')
    load_dotenv(dotenv_path)

    """DEV"""
    """PROD"""

    # Import and execute the command-line utility.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
