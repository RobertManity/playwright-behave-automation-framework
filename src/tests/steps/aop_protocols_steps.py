
from behave import when, then
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect
import re
from src.tests.pages.choose_flask_page import ChooseFlaskPage

from src.tests.pages.aop_page import AoP_Page          # koristiš ga za nav dugmad i NEW PROTOCOL
from src.tests.pages.new_protocol_page import NewProtocolPage  # wizard POM





@then('"NEXT" button is disabled')
@async_run_until_complete
async def step_next_button_disabled(context):
    """Checks that NEXT button inside New Protocol wizard cannot be clicked."""
    await context.new_protocol_page.is_next_disabled()


@then('"CANCEL" button is enabled')
@async_run_until_complete
async def step_cancel_button_enabled(context):
    """Verifies if CANCEL is clickable"""
    await context.new_protocol_page.is_cancel_enabled()


@then('wizard title "Choose Template" is visible')
@async_run_until_complete
async def step_check_choose_template_title(context):
    await context.new_protocol_page.is_choose_template_title_visible()


@when('user clicks on "{menu_item}" button')
@async_run_until_complete
async def step_click_button(context, menu_item):
    """Clicks on the button according to text in feature file."""
    menu_item_upper = menu_item.upper()

    # left menu: HOME / RUNS / MAINTENANCE / PROTOCOLS
    if menu_item_upper in ("HOME", "RUNS", "MAINTENANCE", "PROTOCOLS"):
        await context.aop_page.click_nav_button(menu_item_upper)

    # NEW PROTOCOL button in PROTOCOLS screen
    elif menu_item_upper == "NEW PROTOCOL":
        await context.aop_page.click_new_protocol_button()
        context.new_protocol_page = NewProtocolPage(context.page)
        
    elif menu_item_upper == "NEXT":
        await context.new_protocol_page.click_next()
        context.choose_flask_page = ChooseFlaskPage(context.page)

    elif menu_item_upper == "CANCEL":
        await context.new_protocol_page.click_cancel()

    else:
        raise AssertionError(f"Unknown menu item: {menu_item}")
    

@then('{column_name} column header is visible')
@async_run_until_complete
async def step_column_header_is_visible(context, column_name):
    await context.new_protocol_page.is_column_header_visible(column_name)

@then('protocol name "{expected_name}" is visible')
@async_run_until_complete
async def step_verify_protocol_name(context, expected_name: str):
    locator = context.page.locator("label.mdc-label", has_text=expected_name)
    await expect(locator).to_be_visible()

@then('protocol templates list displays {expected_count:d} items')
@async_run_until_complete
async def step_verify_template_count(context, expected_count: int):
    await context.new_protocol_page.expect_template_count(expected_count)

@then('protocol templates list is visible')
@async_run_until_complete
async def step_protocol_templates_list_is_visible(context):
    await context.new_protocol_page.is_protocol_templates_list_visible()

@when('user navigates to the next page of protocol templates')
@async_run_until_complete
async def step_user_navigates_next_page(context):
    await context.new_protocol_page.click_next_page()

@when('user navigates to the last page of protocol templates')
@async_run_until_complete
async def step_user_navigates_last_page(context):
    await context.new_protocol_page.click_last_page()

@when('user navigates to the first page of protocol templates')
@async_run_until_complete
async def step_user_navigates_first_page(context):
    await context.new_protocol_page.click_first_page()

@when('user navigates to the previous page of protocol templates')
@async_run_until_complete
async def step_user_navigates_previous_page(context):
    await context.new_protocol_page.click_previous_page()

@then('wizard step "{step_label}" is completed')
@async_run_until_complete
async def step_wizard_step_is_completed(context, step_label):
    await context.new_protocol_page.is_wizard_step_completed(step_label)

@when('user selects protocol template "{template_name}"')
@async_run_until_complete
async def step_user_selects_protocol_template(context, template_name: str):
    await context.new_protocol_page.select_protocol_template(template_name)

@then('wizard step "{step_label}" is active')
@async_run_until_complete
async def step_wizard_step_is_active(context, step_label: str):
    await context.new_protocol_page.is_wizard_step_active(step_label)

@then('wizard step "{step_label}" is inactive')
@async_run_until_complete
async def step_wizard_step_is_inactive(context, step_label):
    await context.new_protocol_page.is_wizard_step_inactive(step_label)

@then('flask selection labels are visible and correct')
@async_run_until_complete
async def step_verify_flask_labels(context):
    await context.choose_flask_page.verify_flask_labels()

@then('wizard header displays selected protocol "{template_name}"')
@async_run_until_complete
async def step_wizard_header_displays_selected_protocol(context, template_name: str):
    """Verifies that the wizard header shows the selected protocol name."""
    await context.new_protocol_page.verify_selected_protocol_title(template_name)
