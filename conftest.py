import pathlib
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page(browser_name, base_url):
    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=False)
        context = browser.new_context(record_video_dir=pathlib.Path("videos"), )
        page = context.new_page()
        page.goto(base_url)
        yield page
        page.close()
        context.close()
        browser.close()