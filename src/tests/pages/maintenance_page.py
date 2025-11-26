"""
Maintenance Page POM
"""
from playwright.async_api import Page, expect
from src.tests.pages.base_page import BasePage


class MaintenancePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_header = page.locator("div.header-title span")   

    async def is_page_loaded(self):
        await expect(self.page_header).to_be_visible()
        await expect(self.page_header).to_have_text("Maintenance")
