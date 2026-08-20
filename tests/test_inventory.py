from playwright.sync_api import expect


def test_inventory_page_loads(logged_in_user):

    expect(logged_in_user.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


def test_inventory_title(logged_in_user):

    expect(
        logged_in_user.page.locator(".title")
    ).to_have_text("Products")


def test_logout(logged_in_user):

    logged_in_user.logout()

    expect(logged_in_user.page).to_have_url(
        "https://www.saucedemo.com/"
    )