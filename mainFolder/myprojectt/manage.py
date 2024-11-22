#!/usr/bin/env python
"""

Django's command-line utility for administrative tasks.
This script provides a command-line interface for administrative tasks like
running the server, applying database migrations, creating superusers, etc.

It sets up the environment by configuring the DJANGO_SETTINGS_MODULE and then
delegates command execution to Django's management utilities.

Code written by: Amina Aslam

"""
import os
import sys
from django.core.management import execute_from_command_line


def main():
    """
    Run administrative tasks.

    Sets the DJANGO_SETTINGS_MODULE environment variable to the correct settings
    module for the project and then executes the command-line instructions using
    Django's management framework.

    The function also includes a check to ensure that Django is installed and
    available in the environment. If not, it raises an appropriate ImportError.
    """

    # Set the DJANGO_SETTINGS_MODULE environment variable.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        # Import and run Django's command-line management utility.
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        # If Django is not installed or available, raise an ImportError.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command line arguments provided by the user.
    execute_from_command_line(sys.argv)

    # Debugging line to check if DJANGO_SETTINGS_MODULE is set correctly.
    # in this case it prints the myproject.settings if it is set, otherwise None.
    print(os.environ.get('DJANGO_SETTINGS_MODULE'))


if __name__ == '__main__':
    main()
