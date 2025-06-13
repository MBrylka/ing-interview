import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("browser")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("base_url")

@pytest.fixture(scope="function")
def page(browser_name, base_url):
    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(base_url)
        yield page
        page.close()
        context.close()
        browser.close()