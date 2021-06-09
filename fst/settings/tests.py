from fst.settings.base import *  # noqa


MEDIA_ROOT = oeg('FST_MEDIA_ROOT', PARENT_BASE_DIR / 'media')
STATIC_ROOT = oeg('FST_STATIC_ROOT', PARENT_BASE_DIR / 'static')
TIME_ZONE = 'UTC'
