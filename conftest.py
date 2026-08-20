import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_user(login_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    return InventoryPage(login_page.page)