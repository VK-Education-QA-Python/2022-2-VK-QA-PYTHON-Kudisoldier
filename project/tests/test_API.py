from utils import generate_user_data
import pytest
import allure


@pytest.mark.API
def test_delete_user(client, database_client):
    """
    Предусловия:
    Пользователь уже есть в БД

    Шаги:
    1. Удалить пользователя через ручку API `DELETE http://<APP_HOST>:<APP_PORT>/api/user/<username>`

    Ожидаемый результат:
    1. Пользователь пропадет из базы данных и запрос вернет 204 статус код

    :param client:
    :param database_client:
    :return:
    """
    with allure.step("Create new user through API"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        res = client.add(name, surname, middle_name, username, password, email)
        assert res.status_code == 210
        assert str(database_client.get_user(username)[0]).split()[0] == username
    with allure.step("Delete user through API"):
        res = client.delete_user(username)
        assert res.status_code == 204
    with allure.step("Ensure that user deleted form database"):
        assert database_client.get_user(username) == []


@pytest.mark.API
def test_change_password(client, database_client):
    """
    Предусловия:
    Пользователь уже есть в БД

    Шаги:
    1. Изменить пароль пользователя через ручку API `PUT http://<APP_HOST>:<APP_PORT>/api/user/<username>/change-password`

    Ожидаемый результат:
    1. Пароль в бд поменяется и запрос вернет 204 статус код

    :param client:
    :param database_client:
    :return:
    """
    with allure.step("Create new user through API"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        res = client.add(name, surname, middle_name, username, password, email)
        assert res.status_code == 210
        assert str(database_client.get_user(username)[0]).split()[0] == username
    with allure.step("Change user password"):
        new_password = 'testnewpass'
        res = client.change_password(username, new_password)
        assert res.status_code == 204  # why is so 204??
    with allure.step("Ensure that user password changed in database"):
        assert str(database_client.get_user(username)[0]).split()[3] == new_password

