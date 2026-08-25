import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
    "product_name",
    [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
    ],
)
def test_add_product_to_cart(logged_in_user, product_name):

    inventory_page = logged_in_user

    inventory_page.add_product_to_cart(product_name)

    inventory_page.verify_product_added(product_name)


def test_remove_product_from_cart(logged_in_user):

    inventory_page = logged_in_user

    product_name = "Sauce Labs Backpack"

    inventory_page.add_product_to_cart(product_name)

    inventory_page.verify_product_added(product_name)

    inventory_page.remove_product_from_cart(product_name)

    product = inventory_page.page.locator(
        ".inventory_item"
    ).filter(
        has_text=product_name
    )

    expect(
        product.get_by_role(
            "button",
            name="Add to cart"
        )
    ).to_be_visible()