from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import time


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
    
def test_checkout_from_products(logged_in_user):
    
    #1. login via fixture
    #2. click add to cart then go to products page afterwards
    #3. expect "REMOVE" from products page
    #4. go to cart page then click checkout button
    #5. fill out info

    inventory_page = logged_in_user

    product_to_add = "Sauce Labs Backpack"
    
    inventory_page.add_product_to_cart(
        product_to_add 
    )
    
    inventory_page.open_product_page(product_to_add)
    
    product_page = ProductPage(inventory_page.page)

    product_page.verify_product_added()
    
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
    
    
def test_multiple_products_checkout_from_inv(logged_in_user):
    
    #1. logged in
    #login via fixture nato.
    
    #2. puntang inventory
    inventory_page = logged_in_user
    
    #3. add lahat ng products sa inventory
    #kailangan mag for loop dito
    products =  [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ]

    for product in products:
        print(product)
    
        inventory_page.add_product_to_cart(
            product
        )
    #verify na nag add ng products talaga.
        inventory_page.verify_product_added(product)
    
    time.sleep(2)
    #4. sa inventory mag checkout (hindi sa products)
    inventory_page.open_cart()
 
    #5. go to cart page then click checkout button
    cart_page = CartPage(inventory_page.page)
    
    #6. fill out info
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
    

def test_validation_all_products(logged_in_user):
    
     #1. logged in
        #login via fixture nato.
        
    #2. puntang inventory
    inventory_page = logged_in_user
    
    #3. add lahat ng products sa inventory
    #kailangan mag for loop dito
    products =  [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ]

    for product in products:
        print(product)
    
        inventory_page.add_product_to_cart(
            product
        )
    #verify na nag add ng products talaga.
        inventory_page.verify_product_added(product)


    #4. sa inventory mag checkout (hindi sa products)
    inventory_page.open_cart()
    
    #5. go to cart page then click checkout button
    cart_page = CartPage(inventory_page.page)
    
    #validation happens here
    for product in products:
        print(product)
        
        cart_page.verify_products_added(product)
 
    #6. fill out info
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

    