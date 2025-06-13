import pathlib
import pytest
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

@pytest.fixture(scope="function")
def page(browser_name, base_url):
    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=True)
        context = browser.new_context(record_video_dir=pathlib.Path("test-results/videos"), )
        page = context.new_page()
        stealth_sync(page)
        page.goto(base_url)
        yield page
        page.close()
        context.close()
        browser.close()