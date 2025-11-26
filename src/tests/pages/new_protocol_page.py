from playwright.async_api import Page, expect
from src.tests.pages.base_page import BasePage
import re
import asyncio
from src.tests.pages.choose_flask_page import ChooseFlaskPage


class NewProtocolPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.choose_template_tab = page.locator("span.step-label", has_text="Choose Template")
        self.choose_flask_tab = page.locator("span.step-label", has_text="Choose Flask")
        self.adjust_parameters_tab = page.locator("span.step-label", has_text="Adjust Parameters")
        self.save_protocol_tab = page.locator("span.step-label", has_text="Save Protocol")
        self.next_button = page.get_by_role("button", name="NEXT")
        self.cancel_button = page.get_by_role("button", name="CANCEL")
        wizard = page.locator("polaris-wizard")
        self.next_button = wizard.get_by_role("button", name="NEXT", exact=True)
        self.cancel_button = wizard.get_by_role("button", name="CANCEL", exact=True)
        self.step_title_choose_template = page.locator("label.step-title", has_text="Choose Template")
        self.protocol_title = page.locator("div.new-protocol-container span.title")
        self.protocols_header = self.page.get_by_role("columnheader", name="PROTOCOLS")
        self.protocol_creator_header = self.page.get_by_role("columnheader", name="PROTOCOL CREATOR")
        self.last_execution_header = self.page.get_by_role("columnheader", name="LAST EXECUTION")
        self.flask_type_header = self.page.get_by_role("columnheader", name="FLASK TYPE")
        self.template_header = self.page.get_by_role("columnheader", name="TEMPLATE")
        self.template_column_header = self.page.locator("div.mat-sort-header-content", has_text="Template")
        self.cells_column_header = self.page.locator("div.mat-sort-header-content", has_text="Cells")
        self.template_rows = page.locator("tbody.mdc-data-table__content tr[role='row']")
        self.template_list = page.locator("table tbody tr")
        self.next_page_button = page.get_by_role("button", name="Next page")
        self.last_page_button = page.get_by_role("button", name="Last page")
        self.first_page_button = page.get_by_role("button", name="First page")
        self.previous_page_button = page.get_by_role("button", name="Previous page")
        self.table_container = page.locator("div.table-container")
        



    async def are_wizard_tabs_visible(self):
        await expect(self.choose_template_tab).to_be_visible()
        await expect(self.choose_flask_tab).to_be_visible()
        await expect(self.adjust_parameters_tab).to_be_visible()
        await expect(self.save_protocol_tab).to_be_visible()


    async def is_step_visible(self, step_label: str):
        """Checks that a wizard step with given label is visible."""
        locator = self.page.locator("span.step-label", has_text=step_label)
        await expect(locator).to_be_visible()

    async def is_next_disabled(self):
        await expect(self.next_button).to_be_disabled()

    async def is_cancel_enabled(self):
        await expect(self.cancel_button).to_be_enabled()

    async def click_cancel(self):
        await self.cancel_button.click()
        await asyncio.sleep(2)

    async def click_next(self):
        """Clicks NEXT button (assumes it's enabled)."""
        await self.next_button.click()

    async def is_choose_template_title_visible(self):
        await expect(self.step_title_choose_template).to_be_visible()

    async def are_protocols_table_headers_visible(self):
        await expect(self.protocols_header).to_be_visible()
        await expect(self.protocol_creator_header).to_be_visible()
        await expect(self.last_execution_header).to_be_visible()
        await expect(self.flask_type_header).to_be_visible()
        await expect(self.template_header).to_be_visible()

    async def is_column_header_visible(self, name: str):
        locator = self.page.locator("div.mat-sort-header-content", has_text=name)
        await expect(locator).to_be_visible()

    async def expect_template_count(self, expected: int):
        await expect(self.template_rows).to_have_count(expected)
        await expect(self.template_rows).to_have_count(5)

    async def is_protocol_templates_list_visible(self):
        """Check that at least one protocol template row is visible"""
        await expect(self.template_list.first).to_be_visible()

    async def click_next_page(self):
        """Clicks on pagination next page button"""
        await self.next_page_button.click()

    async def click_last_page(self):
        """Clicks on pagination last page button"""
        await self.last_page_button.click()
     
    async def click_first_page(self):
        """Clicks on pagination first page button"""
        await self.first_page_button.click()

    async def click_previous_page(self):
        """Clicks on pagination previous page button"""
        await self.previous_page_button.click() 
    
    
    def _get_step_item(self, step_label: str):
        """
        Returns locator for one step-item (line + label) by its text.
        """
        return self.page.locator(
            "div.steps-container div.step-item",
            has=self.page.locator("span.step-label", has_text=step_label)
        )

    async def is_wizard_step_active(self, step_label: str):
        step_item = self._get_step_item(step_label)
        step_line = step_item.locator("hr.step-line")
        step_label_el = step_item.locator("span.step-label")

        pattern = re.compile(r".*\bactive\b.*")
        await expect(step_line).to_have_class(pattern)
        await expect(step_label_el).to_have_class(pattern)

    async def is_wizard_step_completed(self, step_label: str):
        step_item = self._get_step_item(step_label)
        step_line = step_item.locator("hr.step-line")
        step_label_el = step_item.locator("span.step-label")

        # Step is considered completed when it has class "completed"
        completed_pattern = re.compile(r".*\bcompleted\b.*")
        await expect(step_line).to_have_class(completed_pattern)
        await expect(step_label_el).to_have_class(completed_pattern)

        # It should NOT be active anymore
        active_pattern = re.compile(r".*\bactive\b.*")
        await expect(step_line).not_to_have_class(active_pattern)
        await expect(step_label_el).not_to_have_class(active_pattern)

    async def is_wizard_step_inactive(self, step_label: str):
        step_item = self._get_step_item(step_label)
        step_line = step_item.locator("hr.step-line")
        step_label_el = step_item.locator("span.step-label")

        bad = re.compile(r".*\b(active|completed)\b.*")
        await expect(step_line).not_to_have_class(bad)
        await expect(step_label_el).not_to_have_class(bad)

    async def is_wizard_step_inactive(self, step_label: str):
        step_item = self._get_step_item(step_label)
        step_line = step_item.locator("hr.step-line")
        step_label_el = step_item.locator("span.step-label")

        bad = re.compile(r".*\b(active|completed)\b.*")
        await expect(step_line).not_to_have_class(bad)
        await expect(step_label_el).not_to_have_class(bad)

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

    async def verify_selected_protocol_title(self, template_name: str):
        """
        Verifies that wizard header displays the selected protocol template.
        Example expected text: "New Protocol - Passaging 1"
        """
        expected_text = f"New Protocol - {template_name}"
        await expect(self.protocol_title).to_have_text(expected_text)

    