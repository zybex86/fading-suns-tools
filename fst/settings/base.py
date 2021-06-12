import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

oeg = os.environ.get


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PARENT_BASE_DIR = BASE_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = oeg('FST_SECRET_KEY', 'very__secret__key__to__override__on__production__server')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = oeg('FST_DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['*']
MAIN_APP = 'fst'

MEDIA_ROOT = oeg('FST_MEDIA_ROOT', f'/opt/{MAIN_APP}/media')
MEDIA_URL = '/media/'
STATIC_ROOT = oeg('FST_STATIC_ROOT', f'/opt/{MAIN_APP}/static')
STATIC_URL = '/static/'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = oeg('FST_TIME_ZONE', 'Europe/Warsaw')
LOGGING_TIME_ZONE = oeg('FST_LOGGING_TIME_ZONE', 'Europe/Warsaw')
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

LANGUAGES = [
    ('en-us', _('English')),
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'corsheaders',
    'django_docutils',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',

    # Internal apps
    f'{MAIN_APP}.{MAIN_APP}',
    # f'{MAIN_APP}.characters',
    f'{MAIN_APP}.users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '.'.join([MAIN_APP, MAIN_APP, 'urls'])

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

WSGI_APPLICATION = '.'.join([MAIN_APP, MAIN_APP, 'wsgi.application'])


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            '()': f'{MAIN_APP}.{MAIN_APP}.utils.TimezoneFormatter',
            'format': '%(levelname)-9s %(asctime)s - %(name)s :: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': oeg('FST_ROOT_LOG_LEVEL', 'INFO').upper(),
    },
    'loggers': {
        'django': {
            'level': oeg('FST_REQUEST_LOG_LEVEL', 'INFO').upper()
        },
        'django.request': {
            'level': oeg('FST_REQUEST_LOG_LEVEL', 'INFO').upper()
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': oeg('FST_DB_BACKENDS_LOG_LEVEL', 'INFO').upper(),
            'propegate': False
        },
    }
}
