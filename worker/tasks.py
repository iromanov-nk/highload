from __future__ import absolute_import
from celery.utils.log import get_task_logger
from celery import task
from data.models import connection


logger = get_task_logger(__name__)
logger.setLevel('INFO')

@task()
def user_call(url, profile):
    logger.info('Start task')
    row = connection.UserVisit({'user_id': profile['user_id'], 'url': url})
    row.save()
    logger.info('Task end')

