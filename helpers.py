import configs


ENV_FILE = '.env'


def get_environment():

    conf = configs.load(ENV_FILE, defaults={'generals': {
        'TASKS_PER_SECOND': '1'
    }})

    return conf['generals'].dict_props


log_settings = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}