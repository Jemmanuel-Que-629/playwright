from playwright.sync_api import expect
from pages.base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_cart(self):

        self.page.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def verify_product_added(self):

        expect(
            self.page.get_by_role(
                "button",
                name="Remove"
            )
        ).to_be_visible()
        
    def get_product_page_price(self):
        
        product_page_div = self.page.locator(".inventory_details_container")
        
        product_page_price_locator = product_page_div.locator(".inventory_details_price")
        
        product_page_price = product_page_price_locator.text_content()
        
        return product_page_price 
    
    def get_product_minibag_count(self):
            
        product_bag_count_locator = self.page.locator(".shopping_cart_badge")
        expect(product_bag_count_locator).to_be_visible()
        return product_bag_count_locator.text_content()
        