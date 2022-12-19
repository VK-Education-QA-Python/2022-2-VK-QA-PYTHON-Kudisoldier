def test_add_get_user(app_client):
    user_id_from_add = app_client.add_user('Kostya')
    user_id_from_get = app_client.get_user('Kostya', 'id')

    assert user_id_from_add == user_id_from_get


def test_add_existent_user(app_client):
    app_client.add_user('Vasya')
    status_code = app_client.add_user('Vasya')

    assert status_code == 400


def test_get_non_existent_user(app_client):
    status_code = app_client.get_user('Masha', 'id')

    assert status_code == 404


def test_with_age(app_client):
    app_client.add_user('Stepan')

    age = app_client.get_user('Stepan', 'age')
    assert isinstance(age, int)
    assert 18 <= age <= 105


def test_has_surname(app_client, mock_client):
    app_client.add_user('Olya')
    mock_client.add_surname('Olya', 'OLOLOEVA')
    surname = app_client.get_user('Olya', 'surname')
    assert surname == 'OLOLOEVA'


def test_has_no_surname(app_client):
    app_client.add_user('Sveta')

    surname = app_client.get_user('Sveta', 'surname')
    assert surname is None
