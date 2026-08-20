from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")

    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    print("LOGIN TEST PASSED")

    input("Press Enter to close...")

    browser.close()