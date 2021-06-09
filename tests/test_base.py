import warnings

from django.conf import settings


def test_dummy():
    """Fake test for checking proper project configuration"""
    warnings.warn("Using database backend {}.".format(
        settings.DATABASES['default']['ENGINE'].replace('django.db.backends.', '')
    ))
    assert True
