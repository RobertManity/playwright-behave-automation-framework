"""
POM Model PlaywrightPage
"""
import re
from playwright.async_api import Page, expect
from src.tests.pages.base_page import BasePage


class PlaywrightPage(BasePage):
    """"
    Provides functionalities for Playwright page
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.title
    
    async def has_url(self, expected_url: str):
        """asserts page has given url"""
        await expect(self.page).to_have_url(expected_url)

    async def has_url_regex(self, expected_url: str):
        """asserts page has given url via regex"""
        await expect(self.page).to_have_url(re.compile(expected_url))
