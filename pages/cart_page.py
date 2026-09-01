from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

class CartPage(BasePage):

    def go_to_checkout(self):

        self.page.get_by_role(
            "button",
            name="Checkout"
        ).click()

        return CheckoutPage(self.page)
    
    def verify_products_added(self, product_name: str):
        product_div = self.page.locator(
            ".cart_item_label"
        ).filter(
            has_text=product_name
        )

        expect(
            product_div.get_by_role(
                "button",
                name="Remove"
            )
        ).to_be_visible()
        
    def get_cart_price(self, product_name: str):
        
        cart_div = self.page.locator(".cart_item").filter(has_text=product_name)
        
        cart_price_locator = cart_div.locator(".inventory_item_price")
        
        cart_price = cart_price_locator.text_content()
        
        return cart_price 