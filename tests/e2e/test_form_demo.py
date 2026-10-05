from playwright.sync_api import Page, expect


base_url = "https://tap-ht24-testverktyg.github.io/form-demo/"


def test_header(page: Page):
    page.goto(base_url)
    heading = page.get_by_role("heading", name="Registrera dig")

    expect(heading).to_be_visible()


def test_form_not_ok_and_ok(page: Page):
    page.goto(base_url)
    knapp = page.get_by_role("button", name="Ok nu kör vi")
    page.get_by_role("textbox", name="Namn").fill("TestUser")
    page.get_by_role("textbox", name="Födelseår").fill("2001")
    page.get_by_role("textbox", name="E-post").fill("test_user@email.com")

    expect(knapp).to_be_disabled()

    page.get_by_role("textbox", name="Lösenord").fill("12342323")

    expect(knapp).to_be_enabled()

    page.get_by_role("button", name="Ok nu kör vi").click()
