def test_command_window(main_page):
    main_page.search_text("Russia")
    main_page.swipe_suggested("население россии")
    assert main_page.get_fact_result() == '146 млн.'


def test_calculator(main_page):
    main_page.search_text('2+2*2')
    assert int(main_page.get_chat_result()) == (2+2*2)


def test_news_source(main_page):
    settings_page = main_page.open_settings()
    news_source_page = settings_page.open_news_source()
    desired_provider = 'Mail.Ru'
    news_source_page.choice_news_provider(desired_provider)
    assert desired_provider == news_source_page.get_selected_provider()
    settings_page = news_source_page.close()
    main_page = settings_page.close()
    main_page.search_text('News')
    assert main_page.get_audio_name() == 'Новости Mail.ru'


def test_about_setting(main_page, version):
    settings_page = main_page.open_settings()
    about_page = settings_page.open_about()
    assert about_page.get_app_version() == version
    assert about_page.get_app_copyright() == 'Mail.ru Group © 1998–2022. Все права защищены.'


