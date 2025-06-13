from playwright.sync_api import Page

from pages.components.cookies_dialog import CookiesSettings, CookiesDialog

class LandingPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.cookies_dialog = CookiesDialog(page)
        self.cookies_settings = CookiesSettings(page)
    
    def goto(self):
        self.page.goto(self.base_url)