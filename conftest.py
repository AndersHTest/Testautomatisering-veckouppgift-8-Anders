import pytest
from playwright.sync_api import Page


@pytest.fixture
def context(context):
    context.set_default_timeout(5000)
    return context


@pytest.fixture(scope="function", autouse=True)
def before_all(page: Page):
    base_url = "https://lejonmanen.github.io/timer-vue/"
    page.goto(base_url, timeout=5000)