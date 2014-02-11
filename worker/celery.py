from __future__ import absolute_import

from celery import Celery
from helpers import get_environment

settings = get_environment()

app = Celery(__name__)

app.conf.update(
    BROKER_URL=settings.get('BROKER_URL'),
    CELERY_IMPORTS=('worker.tasks', ),
    CELERYD_CONCURRENCY=settings.get('CELERYD_CONCURRENCY'),
    CELERY_DEFAULT_QUEUE=settings.get('CELERY_QUEUE')
)