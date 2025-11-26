"""
POM Model BasePage
"""
from playwright.async_api import Page

class BasePage:
    """"
    Provides base page class for page navigation
    """

    def __init__(self, page: Page):
        self.page = page

    async def navigate_to(self, url: str):
        """Navigates to new page"""
        await self.page.goto(url)
