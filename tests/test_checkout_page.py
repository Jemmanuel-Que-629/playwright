from playwright.sync_api import expect

from pages.cart_page import CartPage


def test_checkout_information(logged_in_user):

    inventory_page = logged_in_user

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.open_cart()
    cart_page = CartPage(inventory_page.page)

    checkout_page = cart_page.go_to_checkout()

    checkout_page.fill_customer_information(
        "Jemmanuel",
        "Que",
        "4027"
    )

    checkout_page.continue_to_checkout_overview()

    expect(
        checkout_page.page.locator(".title"),
        "Checkout page title is incorrect"
    ).to_have_text("Checkout: Overview")