"""
Environment that defines setup and teardown functions for the test suite
"""

from playwright.async_api import async_playwright
from behave.api.async_step import async_run_until_complete

@async_run_until_complete
async def before_scenario(context, scenario):
    """
    Setup (runs before every scenario)
    """
    print("Inside before scenario")
    context.p = await async_playwright().start()

    # if scenario.tags.__contains__("UI"):
    browser = await context.p.chromium.launch(headless=False)
    # Flag ignore_https_errors=True is necessary for AoP to ignore
    # https certificate errors
    browser_context = await browser.new_context(ignore_https_errors=True)
    context.page = await browser_context.new_page()
    print(scenario)

@async_run_until_complete
async def after_scenario(context, scenario):
    """
    Teardown (runs after every scenario)
    """
    await context.p.stop()
    print(scenario)
