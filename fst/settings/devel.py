from fst.settings.base import *  # noqa


DEBUG = oeg('FST_DEBUG', 'True').lower() == 'true'
AUTH_BASSWORD_VALIDATORS = []
MEDIA_ROOT = oeg('FST_MEDIA_ROOT', PARENT_BASE_DIR / 'media')
STATIC_ROOT = oeg('FST_STATIC_ROOT', PARENT_BASE_DIR / 'static')
