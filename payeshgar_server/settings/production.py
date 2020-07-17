from .common import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[{asctime}] {levelname} {name} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'standard',
            'facility': 'local0',
            'address': '/dev/log'
        }
    },
    'root': {
        'handlers': [],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['syslog'],
            'level': "ERROR",
            'propagate': False,
        },
        'payeshgar': {
            'handlers': ['syslog'],
            'level': os.getenv("PAYESHGAR_LOG_LEVEL", "INFO"),
            'propagate': False,
        },

    },
}
