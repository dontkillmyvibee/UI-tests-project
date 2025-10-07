import pytest
from playwright.sync_api import Page, Playwright

from _pytest.fixtures import SubRequest

from tools.playwright.pages import initialize_playwright_page
from config import settings


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )
