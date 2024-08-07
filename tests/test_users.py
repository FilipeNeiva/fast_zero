from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    user = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert user['username'] == 'testusername'
    assert user['email'] == 'test@test.com'
    assert user['id'] == 1
    assert 'created_at' in user


def test_create_user_with_username_exist(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'teste2@test.com',
            'password': 'testtest',
        },
    )

    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_with_email_exist(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'Teste2',
            'email': user.email,
            'password': 'testtest',
        },
    )

    assert response.json() == {'detail': 'Email already exists'}


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    user_schema['created_at'] = user.created_at.strftime(
        '%Y-%m-%dT%H:%M:%S.%f'
    )
    user_schema['updated_at'] = user.updated_at.strftime(
        '%Y-%m-%dT%H:%M:%S.%f'
    )
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    response_user = response.json()

    assert response_user['username'] == 'testusername2'
    assert response_user['email'] == 'test@test.com'
    assert response_user['id'] == 1
    assert response_user['created_at'] != response_user['updated_at']


def test_update_wrong_user(client, other_user, token):
    response = client.put(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


def test_read_user_by_id(client, user):
    response = client.get('/users/1')

    response_user = response.json()

    assert response_user['username'] == user.username
    assert response_user['email'] == user.email
    assert response_user['id'] == user.id
    assert 'created_at' in response_user


def test_read_user_by_id_nonexistent(client):
    response = client.get('/users/2')

    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.json() == {'message': 'User deleted'}


def test_delete_wrong_user(client, other_user, token):
    response = client.delete(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}
