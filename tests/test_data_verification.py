from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_inventory_product_price_cart_validation(logged_in_user):
    
    inventory_page = logged_in_user
    
    product_test = "Sauce Labs Backpack"
    
    inventory_page.add_product_to_cart(product_test)
    
    inventory_price = inventory_page.get_inventory_price(product_test)
    
    #need pumuntang product page
    product_page = inventory_page.open_product_page(product_test)
    
    product_price = product_page.get_product_page_price()
    
    assert inventory_price == product_price, "Inventory Price not equal to Product Price or vice versa."
    
    #go to cart page and assert again.
    
    inventory_page.open_cart()
    cart_page = CartPage(inventory_page.page)
    
    cart_price = cart_page.get_cart_price(product_test)

    assert product_price == cart_price, "Product price not equal to cart price."

def test_minibag_count(logged_in_user):
    
    # 1. logged in
    # 2. add product dalawa
    # 3. bilangin sa minibag yung bilang  sa inventory page
    # 4. bilangin sa minibag yung bilang  sa product page
    # 5. assertion kung parehas nga ba talaga.
    
    
    inventory_page = logged_in_user
    
    products = ["Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]
    
    # inventory_page.add_product_to_cart(product1)
    # inventory_page.add_product_to_cart(product2)
    
    for product in products:
        
        inventory_page.add_product_to_cart(
            product
        )
        
    expected_minibag_count = str(len(products))
    
    inventory_page_minibag_counter = inventory_page.get_inventory_minibag_count()
    
    assert inventory_page_minibag_counter == expected_minibag_count, "tamang bilang sa inventory page."
    
    product_page1 = inventory_page.open_product_page(products[0])
    
    product_page1_minibag_counter = product_page1.get_product_minibag_count()
    
    assert product_page1_minibag_counter == expected_minibag_count, f"tamang bilang sa product page {products[0]}"
    
    print(expected_minibag_count, inventory_page_minibag_counter, product_page1_minibag_counter)