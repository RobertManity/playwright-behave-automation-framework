"""
Step definition for playwright
"""

from behave import given, when, then
from behave.api.async_step import async_run_until_complete

from src.tests.pages.ecosia_page import EcosiaPage
from src.tests.pages.playwright_page import PlaywrightPage

@given('Ecosia is open in browser')
@async_run_until_complete
async def ecosia_is_open_in_browser(context):
    """Open Ecosia page"""
    context.ecosia_page = EcosiaPage(context.page)
    await context.ecosia_page.navigate_to('https://ecosia.org')

@when('user confirms cookie dialog')
@async_run_until_complete
async def user_confirms_cookie_dialog(context):
    """confirm cookie banner"""
    await context.ecosia_page.click_cookie_disagree_button()

@when('user adds "{search}" search term')
@async_run_until_complete
async def user_adds_search_term(context, search):
    """enter item to search for"""
    await context.ecosia_page.enter_search_text(search)

@when('user clicks on search button')
@async_run_until_complete
async def user_clicks_search_button(context):
    """click search button"""
    await context.ecosia_page.click_search_button()

@when('user clicks on search result link "{result_link_text}"')
@async_run_until_complete
async def user_clicks_result_link(context, result_link_text):
    """click result link"""
    await context.ecosia_page.click_result_link(result_link_text)

@then('page is shown with url "{expected_url}"')
@async_run_until_complete
async def page_has_url(context, expected_url):
    """click result link"""
    context.playwright_page = PlaywrightPage(context.page)
    await context.playwright_page.has_url(expected_url)

