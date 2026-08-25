from playwright.sync_api import expect


def test_add_backpack_to_cart(logged_in_user):

    page = logged_in_user.page

    products = page.locator(".inventory_item")

    backpack = products.filter(
        has_text="Sauce Labs Backpack"
    )

    add_to_cart = backpack.get_by_role(
        "button",
        name="Add to cart"
    )

    add_to_cart.click()

    expect(
        backpack.get_by_role("button", name="Remove")
    ).to_be_visible()