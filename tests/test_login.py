import pytest
from playwright.sync_api import expect


def test_valid_login(login_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "wrong_password"),
        ("wrong_user", "secret_sauce"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
)
def test_invalid_login(login_page, username, password):

    login_page.open()

    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()