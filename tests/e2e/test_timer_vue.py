from playwright.sync_api import Page, expect

base_url = "https://lejonmanen.github.io/timer-vue/"


def test_add_move_remove_widgets(page: Page):
    page.goto(base_url)
    page.get_by_role("button", name="Add timer").click()
    page.get_by_role("button", name="Add note").click()

    expect(page.get_by_role("heading", name="Break 🖊️")).to_be_visible()

    page.locator("polyline").nth(1).click()
    #TODO Kontrollera att anteckningen ligger ovanför timern. Hur då?

    page.get_by_text("🗑️").nth(1).click()
    page.get_by_text("🗑️").click()

    expect(page.get_by_role("heading", name="Break 🖊️")).not_to_be_visible()
    expect(page.get_by_role("button", name="Click to change text")).not_to_be_visible()


def test_change_timer_value(page: Page):
    page.goto(base_url)
    page.get_by_role("button", name="Add timer").click()
    page.get_by_text("⚙️️").click()
    page.get_by_role("textbox").fill("20")
    page.get_by_role("button", name="Reset").click()
    page.get_by_role("button", name="Start").click()

    expect(page.get_by_role("button", name="Pause")).to_be_visible()

    page.get_by_role("button", name="Pause").click()

    expect(page.get_by_role("button", name="Start")).to_be_visible()

    page.get_by_role("button", name="Reset").click()

    expect(page.get_by_text("20:00")).to_be_visible()

def test_add_note(page: Page):
    page.goto(base_url)
    page.get_by_role("button", name="Add note").click()
    page.get_by_role("heading", name="Click to change text").click()
    page.get_by_role("textbox", name="Description").fill("test")
    page.get_by_role("textbox", name="Description").press("Enter")

    expect(page.get_by_role("heading", name="test")).to_be_visible()


def test_theme(page: Page):
    page.goto(base_url)
    page.get_by_role("button", name="Dark").click()

    expect(page.locator("html")).to_have_attribute("data-theme", "dark")
