import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_fixture():
    User = get_user_model()
    user = User.objects.create_user(
        username='basic_user',
        password='test'
    )

    return user
