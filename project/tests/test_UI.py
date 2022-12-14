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
        welcome_page = reg_page.register(name, surname, middle_name, username, email, password)
        assert welcome_page.check_page()
    with allure.step("Ensure that entered data is matched with welcome page"):
        login_name_data = welcome_page.get_login_name_data()
        assert login_name_data.find(f'Logged as {username}') != -1
        assert login_name_data.find(f'User:  {name} {surname}') != -1


@pytest.mark.UI
@pytest.mark.API
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


@pytest.mark.UI
@pytest.mark.API
def test_vkid(welcome_page, database_client, client, mock_client):
    """
    Предусловия:
    Пользователь уже авторизован в системе

    Пользователь есть в БД mock’a

    Шаги:
    1. Перейти на главную страницу /welcome

    Ожидаемый результат:
    1. В правом верхнем углу будет присутствовать **VK ID: <id>**

    :param welcome_page:
    :param database_client:
    :param client:
    :param mock_client:
    :return:
    """
    with allure.step("Create new user through API"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        res = client.add(name, surname, middle_name, username, password, email)
        assert res.status_code == 210
    with allure.step("Add for created user vk id in mock"):
        vk_id = 5
        assert mock_client.put(username, vk_id).status_code == 201
        assert mock_client.get(username).json['vk_id'] == vk_id
    with allure.step("Assert that user have vk id"):
        session = client.get_session_cookie(username, password)
        welcome_page.driver_load_requests_session(session)
        welcome_page.open()
        assert welcome_page.get_login_name_data().find(f'VK ID: {vk_id}') != -1
    with allure.step("Delete vk id from mock"):
        assert mock_client.delete(username).status_code == 204
    with allure.step("Reload page and ensure that vkid isn't displayed"):
        welcome_page.reload_page()
        assert welcome_page.get_login_name_data().find(f'VK ID: {vk_id}') == -1


@pytest.mark.UI
@pytest.mark.API
def test_block(welcome_page, database_client, client):
    """
    Предусловия:
    Пользователь уже есть в БД

    Шаги:
    1. Зайти на главную страницу по адресу /welcome
    2. Заблокировать пользователя через ручку `api/user/{username}/block`

    Ожидаемый результат:
    1. Откроется главная страница приложения
    2. Пользователь выйдет из сессии и больше не сможет пользоваться сайтом

    :param welcome_page:
    :param database_client:
    :param client:
    :return:
    """
    with allure.step("Create new user through API"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        res = client.reg(name, surname, middle_name, username, password, email)
        assert res.status_code == 200
    with allure.step("Open welcome page"):
        session = client.get_session_cookie(username, password)
        welcome_page.driver_load_requests_session(session)
        welcome_page.open()
    with allure.step("Block user from API"):
        assert client.block_user(username).status_code == 200
    with allure.step("Ensure that user blocked in database"):
        assert int(str(database_client.get_user(username)[0]).split()[4]) == 0
    with allure.step("Ensure that user cannot access UI"):
        welcome_page.open()
        with pytest.raises(AssertionError):
            assert welcome_page.check_page()


@pytest.mark.API
@pytest.mark.UI
def test_unblock(welcome_page, database_client, client):
    """
    Предусловия:
    Пользователь уже есть в БД
    Пользователь уже заблокирован

    Шаги:

    1. Разблокировать пользователя через ручку `api/user/{username}/accept`
    2. Войти в приложение с данными разблокированного пользователя

    Ожидаемый результат:
    1. Пользователю не будут доступны функции приложения и его выкинет на экран входа
    2. Пользователь успешно войдет в систему и сможет пользоваться функционалом

    :param welcome_page:
    :param database_client:
    :param client:
    :return:
    """
    with allure.step("Create new user through API"):
        name, surname, username, email, password, middle_name,\
        access, active, start_active_time = generate_user_data()
        res = client.reg(name, surname, middle_name, username, password, email)
        assert res.status_code == 200
    with allure.step("Block user from DB"):
        database_client.block_user(username)
    with allure.step("Open welcome page"):
        session = client.get_session_cookie(username, password)
        welcome_page.driver_load_requests_session(session)
        welcome_page.open()
    with allure.step("Ensure that user cannot access UI"):
        with pytest.raises(AssertionError):
            assert welcome_page.check_page()
    with allure.step("Unblock user with API"):
        name2, surname2, username2, email2, password2, middle_name2,\
        access2, active2, start_active_time2 = generate_user_data()
        assert client.reg(name2, surname2, middle_name2, username2, password2, email2).status_code == 200
        assert client.unblock_user(username).status_code == 200
    with allure.step("Login again and check that everything is OK"):
        assert client.login(username, password).status_code == 200
        session = client.get_session_cookie(username, password)
        welcome_page.driver_load_requests_session(session)
        welcome_page.open()
        assert welcome_page.check_page()

