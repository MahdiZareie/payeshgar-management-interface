import sys

from .common import *

SECRET_KEY = os.getenv("PAYESHGAR_SECRET_KEY")

TEST_ENVIRONMENT = 'test' in sys.argv

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'monitoring',
    'inspecting',
    'security',

    'rest_framework',
    'rest_framework_jwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'payeshgar_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'payeshgar_server.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = False

STATIC_URL = '/static/'

CELERY_BROKER_URL = "amqp://{rabbitmq_hostname}:{rabbitmq_port}".format(
    rabbitmq_hostname=os.environ.get("PAYESHGAR_RABBITMQ_HOSTNAME", "localhost"),
    rabbitmq_port=os.environ.get("PAYESHGAR_RABBITMQ_PORT", "5672"),
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

ENVIRONMENT = os.getenv("PAYESHGAR_ENVIRONMENT", "PRODUCTION")
if TEST_ENVIRONMENT:
    ENVIRONMENT = "TEST"
    from .test import *
else:
    if ENVIRONMENT == "PRODUCTION":
        from .production import *
    elif ENVIRONMENT == "DEVELOPMENT":
        from .development import *

try:
    from payeshgar_server.settings.local_settings import *
except:
    pass
