"""
POM Model AoP_Page
"""
from playwright.async_api import Page, expect
from src.tests.pages.base_page import BasePage

class AoP_Page(BasePage):
    """"
    Provides functionalities for AoP page
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.home_button = page.get_by_role("link", name="HOME")
        self.runs_button = page.get_by_role("link", name="RUNS")
        self.maintenance_button = page.get_by_role("link", name="MAINTENANCE")
        self.protocols_button = page.get_by_role("link", name="PROTOCOLS")
        self.current_datetime = page.locator("polaris-current-date-time.time span")
        self.hamilton_logo = page.locator("img.header-logo")
        self.header_title = page.locator("span.header-title-desktop")
        self.new_protocol_button = page.get_by_role("button", name="NEW PROTOCOL")
        self.no_protocols_text = page.locator("div.no-data-banner-text")
        self.header_time = page.locator("polaris-current-date-time.time span")



    async def click_on_button(self, button_text: str):
        """"Click on the aop button with given text"""
        match button_text:
            case 'HOME':
                await self.home_button.click()
            case 'RUNS':
                await self.runs_button.click()
            case  'MAINTENANCE':
                await self.maintenance_button.click()
            case 'PROTOCOLS':
                await self.protocols_button.click()
            case _:
                pass
    
    async def has_url(self, expected_url: str):
        """asserts page has given url"""
        #wait for 1.5 sec for demo purposes, this should not be applied
        #on productive code
        await self.page.wait_for_timeout(1500)
        await expect(self.page).to_have_url(expected_url)

    async def assert_header_datetime_format(self):
        from datetime import datetime
        await expect(self.current_datetime).to_be_visible()
        text = (await self.current_datetime.text_content()).strip()
        datetime.strptime(text, "%d-%b-%y %H:%M") 


    async def is_home_visible(self):
        await expect(self.page.get_by_role("link", name="HOME")).to_be_visible()

    async def is_runs_visible(self):
        await expect(self.page.get_by_role("link", name="RUNS")).to_be_visible()

    async def is_maintenance_visible(self):
        await expect(self.page.get_by_role("link", name="MAINTENANCE")).to_be_visible()

    async def is_protocols_visible(self):
        await expect(self.page.get_by_role("link", name="PROTOCOLS")).to_be_visible()
    
    async def is_logo_visible(self):
        """Asserts that Hamilton logo is visible in the left header."""
        await expect(self.hamilton_logo).to_be_visible()

    async def verify_logo_attributes(self):
        """Checks src, width i height atributa iz HTML-a."""
        await expect(self.hamilton_logo).to_have_attribute("src", "./logo.png")
        await expect(self.hamilton_logo).to_have_attribute("width", "100%")
        await expect(self.hamilton_logo).to_have_attribute("height", "70")

    async def verify_logo_size_rendered(self):
        """Checks real rended size in browser."""
        box = await self.hamilton_logo.bounding_box()
        assert box is not None, "Hamilton logo not found on page"
        assert round(box["width"]) == 100, f"Expected width 100%, got {box['width']}"
        assert round(box["height"]) == 70, f"Expected height 70, got {box['height']}"


    async def click_nav_button(self, menu_item: str):
        """It clicks on specific menu button"""
        menu_item = menu_item.upper()

         # Mapping menu names to their respective page locators
        nav_map = {
            "HOME": self.home_button,
            "RUNS": self.runs_button,
            "MAINTENANCE": self.maintenance_button,
            "PROTOCOLS": self.protocols_button
        }

        # Validate that the provided menu item exists in the navigation map
        if menu_item not in nav_map:
            raise ValueError(f"Unknown menu item: {menu_item}")

         # Perform the click action on the selected locator
        await nav_map[menu_item].click()


    async def header_should_be(self, expected_text: str):
        """
        Validate that the page header text matches the expected value.
        """
        await expect(self.header_title).to_have_text(expected_text)

    async def is_new_protocol_button_visible(self):
        await expect(self.new_protocol_button).to_be_visible()

    async def click_new_protocol_button(self):
        await self.new_protocol_button.click()

    async def is_new_protocol_button_visible(self):
        await expect(self.new_protocol_button).to_be_visible()

    async def is_no_protocols_message_visible(self):
        await self.no_protocols_text.wait_for(state="visible")
        await expect(self.no_protocols_text).to_have_text("There are no created protocols yet.")