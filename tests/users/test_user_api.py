import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


@pytest.mark.django_db
def test_create_valid_user_success(api_client):
    data = {
        'username': 'testuser',
        'password': 'testpass',
        'name': 'Test'
    }
    response = api_client.post(CREATE_USER_URL, data)

    assert response.status_code == status.HTTP_201_CREATED
    user = get_user_model().objects.get(**response.data)
    assert user.check_password(data['password'])
    assert data['password'] not in response.data


@pytest.mark.django_db
@pytest.mark.parametrize('post_data, expected_response', (
    pytest.param({
        'username': 'basic_user',
        'password': 'testpass',
        'name': 'Test'
    }, {
        'username': ['user with this username already exists.']
    }, id='existing_user'),
    pytest.param({
        'password': 'testpass',
        'name': 'Test'
    }, {
        'username': ['This field is required.']
    }, id='no_username'),
    pytest.param({
        'username': '',
        'password': 'testpass',
        'name': 'Test'
    }, {
        'username': ['This field may not be blank.']
    }, id='blank_username'),
))
def test_user_errors(api_client, user_fixture, post_data, expected_response):
    response = api_client.post(CREATE_USER_URL, post_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response
