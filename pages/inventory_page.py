from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class InventoryPage(BasePage):

    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def verify_product_added(self, product_name: str):
        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        expect(
            product.get_by_role(
                "button",
                name="Remove"
            )
        ).to_be_visible()

    def remove_product_from_cart(self, product_name: str):

        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Remove"
        ).click()

    def verify_product_removed(self, product_name: str):

        product = self.page.locator(
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

    def open_product_page(self, product_name: str):

            product_div = self.page.locator(
                ".inventory_item"
            ).filter(
                has_text=product_name
            )
            
            product_page_name_locator = product_div.locator(".inventory_item_name")
            
            product_page_name_locator.click()
            
            return ProductPage(self.page)

    def open_cart(self):

            self.page.locator(
                ".shopping_cart_link",
            ).click()

            return CartPage(self.page)
        
    def get_inventory_price(self, product_name: str):
        
        product_div = self.page.locator(".inventory_item").filter(has_text=product_name)
        
        product_price_locator = product_div.locator(".inventory_item_price")
        
        product_price = product_price_locator.text_content()
        
        return product_price 
    
    def get_inventory_minibag_count(self):
        
        mini_bag_count_locator = self.page.locator(".shopping_cart_badge")
        expect(mini_bag_count_locator).to_be_visible()
        return mini_bag_count_locator.text_content()
