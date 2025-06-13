from pages.landing_page import LandingPage
from playwright.sync_api import TimeoutError

def test_modifying_cookies(page, base_url):

    required_cookie = "cookiePolicyGDPR=3"

    landing_page = LandingPage(page, base_url)
    landing_page.goto()

    landing_page.cookies_dialog.wait_to_appear()

    landing_page.cookies_dialog.open_settings()
    landing_page.cookies_settings.toggle_analytics()
    landing_page.cookies_settings.accept_all()
    
    try:
        page.wait_for_function(f"document.cookie.includes('{required_cookie}')", timeout=5000)
    except TimeoutError:
        raise AssertionError(f"Cookie '{required_cookie}' was not set after accepting cookies.")

