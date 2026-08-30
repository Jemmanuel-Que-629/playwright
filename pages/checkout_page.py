from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def fill_customer_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ):
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)

    def continue_to_checkout_overview(self):
        self.page.locator("#continue").click()