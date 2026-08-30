from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):

    def go_to_checkout(self):

        self.page.get_by_role(
            "button",
            name="Checkout"
        ).click()

        return CheckoutPage(self.page)