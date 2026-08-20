import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
)


@pytest.fixture
def logged_in_user():
    login_page = LoginPage(page)
    login_page.open()

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    return InventoryPage(login_page.page)