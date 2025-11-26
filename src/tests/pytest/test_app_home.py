from playwright.sync_api import Page, expect


def test_home_button_is_visible(page: Page):
    page.goto("https://localhost:5003")
    home_button = page.get_by_role("link", name="HOME")
    expect(home_button).to_be_visible()

def test_runs_button_is_visible(page: Page):
    page.goto("https://localhost:5003")

    runs_button = page.get_by_role("link", name="RUNS")
    expect(runs_button).to_be_visible()


def test_protocols_button_is_visible(page: Page):
    page.goto("https://localhost:5003")

    protocols_button = page.get_by_role("link", name="PROTOCOLS")
    expect(protocols_button).to_be_visible()


def test_maintenance_button_is_visible(page: Page):
    page.goto("https://localhost:5003")

    maintenance_button = page.get_by_role("link", name="MAINTENANCE")
    expect(maintenance_button).to_be_visible()

def test_all_nav_buttons_are_visible(page: Page):
    page.goto("https://localhost:5003")

    nav_items = ["HOME", "RUNS", "PROTOCOLS", "MAINTENANCE"]

    for item in nav_items:
        button = page.get_by_role("link", name=item)
        expect(button).to_be_visible()