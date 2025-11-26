"""
Step definition for AoP
"""

from behave import given, when, then
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect
import re
from src.tests.pages.aop_page import AoP_Page
from src.tests.pages.new_protocol_page import NewProtocolPage
from src.tests.pages.protocols_page import ProtocolsPage
from datetime import datetime
from behave import then
from behave.api.async_step import async_run_until_complete


@given('AoP is open')
@async_run_until_complete
async def ecosia_is_open_in_browser(context):
    """Open AoP"""
    context.aop_page = AoP_Page(context.page)
    await context.aop_page.navigate_to('https://localhost:5003')

# @when('user clicks on "{button_text}" button')
# @async_run_until_complete
# async def user_confirms_cookie_dialog(context, button_text:str):
#     """confirm cookie banner"""
#     await context.aop_page.click_on_button(button_text)

@then('page has url  "{expected_url}"')
@async_run_until_complete
async def page_has_url(context, expected_url:str):
    """confirm cookie banner"""
    await context.aop_page.has_url(expected_url)

@then('HOME is visible')
@async_run_until_complete
async def home_screen_is_visible(context):
    """Ensures Home is visible"""
    await context.aop_page.is_home_visible()
    
@then('RUNS is visible')
@async_run_until_complete
async def runs_screen_is_visible(context):
    """Ensures Runs  is visible"""
    await context.aop_page.is_runs_visible()

@then('MAINTENANCE is visible')
@async_run_until_complete
async def maintenance_screen_is_visible(context):
    """EnsuresMainentance Screen is visible"""
    await context.aop_page.is_maintenance_visible()    

@then('PROTOCOLS is visible')
@async_run_until_complete
async def protocols_screen_is_visible(context):
    """Ensures Protocols is visible"""
    await context.aop_page.is_protocols_visible()    


@then("current date and time is shown in correct format")
@async_run_until_complete
async def step_impl(context):
    """Ensures Date and Time have correct format """
    await context.aop_page.assert_header_datetime_format()

@then("the current date and time should be visible")
@async_run_until_complete
async def step_datetime_is_visible(context):
    await expect(context.aop_page.current_datetime).to_be_visible()

@then('the format should match "DD-MMM-YY HH:MM"')
@async_run_until_complete
async def step_datetime_correct_format(context):
    await context.aop_page.assert_header_datetime_format()

@then("the month abbreviation should start with a capital letter")
@async_run_until_complete
async def step_month_uppercase(context):
    text = (await context.aop_page.current_datetime.text_content()).strip()
    month = text.split("-")[1]  # Example: "Nov"
    assert month[0].isupper() and month[1:].islower(), \
        f"Invalid month formatting in datetime: {month}"
    
@when("the user looks at the top header section of the application")
@async_run_until_complete
async def step_look_at_header(context):

    pass

@then("Hamilton logo is visible")
@async_run_until_complete
async def hamilton_logo_visible(context):
    await context.aop_page.is_logo_visible()

@then("Hamilton logo has correct size and source")
@async_run_until_complete
async def hamilton_logo_correct_details(context):
    await context.aop_page.verify_logo_attributes()
    await context.aop_page.verify_logo_size_rendered()

@when('Protocols page is opened')
@async_run_until_complete
async def step_open_protocols(context):
    """Instantiate ProtocolsPage after navigating to Protocols screen."""
    context.protocols_page = ProtocolsPage(context.page)

@then('page header is "{header_text}"')
@async_run_until_complete
async def step_page_header_is(context, header_text):
    """Validation Header is changed"""
    await context.aop_page.header_should_be(header_text)

@then('button "NEW PROTOCOL" is visible')
@async_run_until_complete
async def step_new_protocol_button_visible(context):
    """Verifies if NEW PROTOCOL button is visible."""
    await context.aop_page.is_new_protocol_button_visible()
    

@then('wizard step "{step_label}" is visible')
@async_run_until_complete
async def step_verify_wizard_step(context, step_label):
    locator = context.page.locator("polaris-wizard span.step-label").filter(
        has_text=re.compile(rf"\b{re.escape(step_label)}\b")
    )
    await expect(locator).to_be_visible()

@then('Protocols table headers are visible')
@async_run_until_complete
async def step_verify_protocols_headers(context):
    await context.protocols_page.are_protocols_table_headers_visible()

@then('NEW PROTOCOL button is visible')
@async_run_until_complete
async def step_verify_new_protocol_button(context):
    await context.aop_page.is_new_protocol_button_visible()

@then('no protocols message is shown')
@async_run_until_complete
async def step_verify_no_protocols_message(context):
    await context.aop_page.is_no_protocols_message_visible()


@then("current date and time matches local system")
@async_run_until_complete
async def step_verify_current_date_time(context):
    """
    Validates that the header date & time displayed in the UI
    matches the local system time (same date and minute),
    with a small allowed difference.
    """

    # 1) Wait until the header time element becomes visible
    await context.aop_page.header_time.wait_for(state="visible")

    # 2) Read text from UI, e.g. "24-Nov-25 14:47"
    ui_text = (await context.aop_page.header_time.text_content()).strip()

    # 3) Parse UI text -> datetime using displayed format
    ui_datetime = datetime.strptime(ui_text, "%d-%b-%y %H:%M")

    # 4) Current local system datetime
    local_datetime = datetime.now()

    # 5) Allowed difference in seconds (UI has no seconds, so up to <60s)
    allowed_seconds = 60

    diff_seconds = abs((local_datetime - ui_datetime).total_seconds())

    # 6) Assert that UI time is close enough to local system time
    assert diff_seconds <= allowed_seconds, (
        f"Date/Time mismatch! UI shows {ui_text}, "
        f"system time is {local_datetime.strftime('%d-%b-%y %H:%M')}, "
        f"difference = {diff_seconds:.1f} seconds (allowed: {allowed_seconds}s)"
    )

    