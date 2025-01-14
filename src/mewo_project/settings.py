import configparser
import logging
import os
import sys

from .helpers.config import EnvOrParserConfig

_config = configparser.RawConfigParser()

if 'PRETIX_CONFIG_FILE' in os.environ:
    _config.read_file(open(os.environ.get('PRETIX_CONFIG_FILE'), encoding='utf-8'))
else:
    _config.read(['/etc/pretix/pretix.cfg', os.path.expanduser('~/.pretix.cfg'), 'pretix.cfg'],
                 encoding='utf-8')
    
config = EnvOrParserConfig(_config)
CONFIG_FILE = config
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = config.get('mewo', 'datadir', fallback=os.environ.get('DATA_DIR', 'data'))
LOG_DIR = os.path.join(DATA_DIR, 'logs')
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
PROFILE_DIR = os.path.join(DATA_DIR, 'profiles')

debug_fallback = "runserver" in sys.argv
DEBUG = config.getboolean('django', 'debug', fallback=debug_fallback)
loglevel = 'DEBUG' if DEBUG else config.get('mewo', 'loglevel', fallback='INFO')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(name)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': loglevel,
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': loglevel,
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': loglevel,
            'propagate': True,
        },
        'django.security': {
            'handlers': ['console'],
            'level': loglevel,
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',  # Do not output all the queries
            'propagate': False,
        },
        'asyncio': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
}