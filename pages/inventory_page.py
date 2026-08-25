from playwright.sync_api import expect
from pages.base_page import BasePage


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