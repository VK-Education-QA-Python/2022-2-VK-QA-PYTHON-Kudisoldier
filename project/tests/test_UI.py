from utils import generate_user_data
import pytest
import allure


@pytest.mark.UI
def test_login(login_page, database_client):
    """
    Предусловия:
    Пользователь с <username> johndoe2 и <password> 123123 уже зарегистрирован и находится в БД.

    Шаги:
    1. Перейти на страницу входа по адресу /login
    2. В поле username написать ‘johndoe2’
    3. В поле password написать ‘123123’
    4. Нажать на кнопку ‘LOGIN’

    Ожидаемый результат:
    1. Откроется окно входа
    2. В поле username отобразится ‘johndoe2’
    3. В поле password отобразится ‘******’
    4. Откроется главная страница /welcome, в правой верхней части странице **Logged as** <username>, а **User:** <name> <surname>
    :param login_page:
    :return:
    """
    with allure.step("Create user in database"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        database_client.add_user(name, surname, middle_name, username,
                                 password, email, access, active, start_active_time)
    with allure.step("Login created user"):
        assert login_page.login(username, password) == 'success'


@pytest.mark.UI
def test_registration(reg_page):
    """
    Предусловия:
    Пользователь с <username> johndoe2 и <password> 123123 уже зарегистрирован и находится в БД.

    Шаги:
    1. Перейти на страницу входа по адресу /login
    2. В поле username написать ‘johndoe2’
    3. В поле password написать ‘123123’
    4. Нажать на кнопку ‘LOGIN’

    Ожидаемый результат:
    1. Откроется окно входа
    2. В поле username отобразится ‘johndoe2’
    3. В поле password отобразится ‘******’
    4. Откроется главная страница /welcome, в правой верхней части странице **Logged as** <username>, а **User:** <name> <surname>

    :param reg_page:
    :param fake:
    :return:
    """
    with allure.step("Create new user through UI"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        assert reg_page.register(name, surname, middle_name, username, password, email) == 'success'


@pytest.mark.UI
def test_logout(welcome_page, database_client, client):
    """
    Предусловия:
    Пользователь уже авторизован в системе и находится на главной странице по адресу /welcome

    Шаги:
    1. Нажать на кнопку ‘Logout’ в правой верхней части экрана

    Ожидаемый результат:
    1. Откроется окно входа, в базе данных у текущего пользователя поле active станет равным нулю.

    :param welcome_page:
    :param database_client:
    :param client:
    :return:
    """
    with allure.step("Create new user through API"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        res = client.add(name, surname, middle_name, username, password, email)
        assert res.status_code == 210
    with allure.step("Assert that user logged out and active is 0"):
        session = client.get_session_cookie(username, password)
        welcome_page.driver_load_requests_session(session)
        welcome_page.open()
        assert int(str(database_client.get_user(username)[0]).split()[2]) == 1
        login_page = welcome_page.click_logout_button()
        assert login_page.check_page()
        assert int(str(database_client.get_user(username)[0]).split()[2]) == 0

