"""
POM Model: Choose Flask Page
"""

from playwright.async_api import Page, expect
from src.tests.pages.base_page import BasePage

class ChooseFlaskPage(BasePage):

    EXPECTED_FLASK_LABELS = ["Source Flask", "Target Flask", "Pooling Flask"]

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.flask_labels = page.locator("label.flask-label")

    async def verify_flask_labels(self):
        count = await self.flask_labels.count()
        assert count == 3, f"Expected 3 labels, got {count}"

        for index, text in enumerate(self.EXPECTED_FLASK_LABELS):
            await expect(self.flask_labels.nth(index)).to_have_text(text)

    async def select_protocol_template(self, template_name: str):
        """
        Selects a protocol template by its visible label name.
        Example: "Passaging 1"
        """
        # Locate the template label by text
        template_label = self.page.locator("label.mdc-label", has_text=template_name)

        # Ensure the label is visible before clicking
        await expect(template_label).to_be_visible()

        # Click the label to select the template (radio selection is triggered automatically)
        await template_label.click()
