import pytest


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

    logged_in_user.add_product_to_cart(product_name)

    logged_in_user.verify_product_added(product_name)