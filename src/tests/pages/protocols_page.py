"""
POM model for Protocols page
"""

from playwright.async_api import Page, expect
from src.tests.pages.base_page import BasePage


class ProtocolsPage(BasePage):
    """Provides functionalities for Protocols screen."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Table header columns on Protocols screen
        self.protocols_header = page.locator(
            "div.mat-sort-header-content", has_text="Protocols"
        )
        self.protocol_creator_header = page.locator(
            "div.mat-sort-header-content", has_text="Protocol Creator"
        )
        self.last_execution_header = page.locator(
            "div.mat-sort-header-content", has_text="Last Execution"
        )
        self.flask_type_header = page.locator(
            "div.mat-sort-header-content", has_text="Flask Type"
        )
        self.template_header = page.locator(
            "div.mat-sort-header-content", has_text="Template" 
        )

    async def are_protocols_table_headers_visible(self):
        await expect(self.protocols_header).to_be_visible()
        await expect(self.protocol_creator_header).to_be_visible()
        await expect(self.last_execution_header).to_be_visible()
        await expect(self.flask_type_header).to_be_visible()
        await expect(self.template_header).to_be_visible()
