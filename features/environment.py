# features/environment.py

from behave import use_fixture

from config.test_behave import browser_chrome
from config.driver_setup import close_driver, setup_driver


def before_all(context):
    # Perform setup actions before the entire test suite runs
    context.driver = setup_driver()

    # Use the browser_chrome fixture for all scenarios
    context.driver = use_fixture(browser_chrome, context)


def after_all(context):
    # Perform teardown actions after the entire test suite runs
    close_driver(context.driver)


def before_scenario(context, scenario):
    pass
    # if "@special_setup" in scenario.effective_tags:
        # Special setup code for scenarios with the "@special_setup" tag


def after_scenario(context, scenario):
    # Scenario-specific teardown code
    pass
