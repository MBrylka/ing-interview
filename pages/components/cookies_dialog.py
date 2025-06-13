from playwright.sync_api import Page, Locator

class CookiesDialog:
    def __init__(self, page: Page):
        self.page = page
        self.modify_button: Locator = page.locator("button:has-text('Dostosuj')")

    def open_settings(self):
        self.modify_button.click()

    def wait_to_appear(self):
        self.page.wait_for_selector("button:has-text('Dostosuj')", state="visible", timeout=10000)
        if not self.modify_button.is_visible():
            raise TimeoutError("Cookies dialog did not appear in time.")

class CookiesSettings:
    def __init__(self, page: Page):
        self.page = page
        self.analytics_checkbox: Locator = page.locator("[name='CpmAnalyticalOption']")
        self.accept_button: Locator = page.locator("button:has-text('Zaakceptuj zaznaczone')")

    def toggle_analytics(self):
        if not self.analytics_checkbox.is_checked():
            self.analytics_checkbox.click()

    def accept_all(self):
        self.accept_button.click()
        self.page.wait_for_timeout(6000)