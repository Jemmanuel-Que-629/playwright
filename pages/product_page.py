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