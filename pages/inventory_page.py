from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.get_by_role("link", name="Logout")

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()