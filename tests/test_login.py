import pytest
from playwright.sync_api import expect

from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_LOGIN_SCENARIOS,
)


def test_valid_login(login_page):

    login_page.open()

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.page).to_have_url(
        f"{login_page.URL}/inventory.html"
    )


@pytest.mark.parametrize(
    "username,password",
    INVALID_LOGIN_SCENARIOS,
)
def test_invalid_login(login_page, username, password):

    login_page.open()

    login_page.login(username, password)

    expect(
        login_page.error_message
    ).to_be_visible()


@pytest.mark.parametrize("burger_item, correct_burger_item_link", [
    ('All Items', 'https://www.saucedemo.com/inventory.html#'),
    ('About', 'https://saucelabs.com/'),
    ('Logout', 'https://www.saucedemo.com/'),
    ('Reset App State', 'https://www.saucedemo.com/inventory.html')
])
def test_menu_burgers_clickable(logged_in_user, burger_item, correct_burger_item_link):

    logged_in_user.menu_button.click()

    logged_in_user.page.get_by_role(
        "link",
        name=burger_item
    ).click()

    #logged_in_user.page.wait_for_load_state("networkidle")

    # 1. login - no need bcos addressed via fixture
    # 2. click burger icon
    # 3. click burger_item
    # 4. validate that user is redirected to correct_burger_item_link