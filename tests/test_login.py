from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_valid_login(login_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    inventory_page = InventoryPage(login_page.page)

    inventory_page.logout()

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/"
    )