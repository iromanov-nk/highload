from __future__ import absolute_import

import time
import random
import logging
import logging.config

from celery.execute import send_task

from helpers import get_environment, log_settings


def get_random_urls():
    count = 0
    urls = [
        'auth',
        'login',
        'feed',
        'profile',
        'logout'
    ]
    while count < settings.get('TASKS_PER_SECOND'):
        random.shuffle(urls)
        url = '/'.join(urls)
        profile = {
            'user_id': random.randrange(1, 10),
        }
        count += 1
        yield url, profile


if __name__ == '__main__':
    settings = get_environment()

    logging.config.dictConfig(log_settings)
    logger = logging.getLogger('scribe')
    logger.info('Start scribe service')
    while True:
        for url, profile in get_random_urls():
            send_task("worker.tasks.user_call", [url, profile],
                      queue=settings.get('CELERY_QUEUE'))
        logger.info('Generate {0} user request'.format(settings.get('TASKS_PER_SECOND')))
        time.sleep(1)