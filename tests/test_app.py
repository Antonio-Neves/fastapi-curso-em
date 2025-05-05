# import pytest
# from fastapi.testclient import TestClient
from http import HTTPStatus

# from fast_zero.app import app


def test_root_must_return_ok_and_obrigado(client):

    response = client.get('/')  # Action

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Obrigado meu Deus'}  # Assert


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'testpassword'
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1
    }


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1
            }
        ]
    }

