from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_role(
            "button",
            name="Open Menu"
        )

        self.logout_link = page.get_by_role(
            "link",
            name="Logout"
        )

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()