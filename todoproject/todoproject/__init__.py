from __future__ import absolute_import, unicode_literals
import django

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as todoproject_app

__all__ = ('todoproject_app',)