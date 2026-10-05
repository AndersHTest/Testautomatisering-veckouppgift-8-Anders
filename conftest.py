import pytest
from playwright.sync_api import Page


@pytest.fixture
def context(context):
    # tal kan skrivas vanligt (1000) eller med tusentals-separator (1_000)
    context.set_default_timeout(1_000)
    return context


@pytest.fixture(scope="function", autouse=True)
def before_all(page: Page):
    base_url = "https://lejonmanen.github.io/agile-helper/"
    page.goto(base_url, timeout=30_000)