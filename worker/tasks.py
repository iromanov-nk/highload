from __future__ import absolute_import
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
logger.setLevel('INFO')

@task()
def user_call(url, profile):
    logger.info('Start task')

