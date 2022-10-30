import pytest
import time


def test_command_window(main_page):
    main_page.search_text("Russia")
    main_page.swipe_suggested("население россии")
    assert main_page.get_fact_result() == '146 млн.'


