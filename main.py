#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from home.models import *
