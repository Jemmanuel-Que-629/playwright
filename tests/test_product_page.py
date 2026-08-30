import pytest

def test_add_product_from_product_page(inventory_page):

    product_page = inventory_page.open_product_page(
        "Sauce Labs Backpack"
    )

    product_page.add_product_to_cart()

    product_page.verify_product_added()