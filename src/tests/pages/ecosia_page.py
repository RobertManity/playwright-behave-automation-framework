"""
POM Model EcosiaPage
"""
from playwright.async_api import Page
from src.tests.pages.base_page import BasePage

class EcosiaPage(BasePage):
    """"
    Provides functionalities for Ecosia page
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.cookie_disagree_button = page.locator("button[id=\"didomi-notice-disagree-button\"]")
        self.search_input = page.locator("input[class=\"search-form__input\"]")
        self.search_button = page.locator("button[data-test-id=\"search-form-submit\"]")

    async def enter_search_text(self, search_text: str):
        """"Enter search text in search input field"""
        await self.search_input.fill(search_text)

    async def click_cookie_disagree_button(self):
        """"Click on the 'disagree' cookie button"""
        await self.cookie_disagree_button.click()

    async def click_search_button(self):
        """"Click on the 'search' button"""
        await self.search_button.click()
        await self.page.wait_for_load_state("networkidle")

    async def click_result_link(self, result_link: str):
        """Click on first result link with given text"""
        first_link = self.page.get_by_role(
            "link",
            name=result_link, exact=True).first
        await first_link.scroll_into_view_if_needed()
        await first_link.click()
        await self.page.wait_for_load_state("networkidle")

