# config/test_behave.py

from behave import fixture

from config.driver_setup import setup_driver, close_driver


# Fixture to set up and tear down the Selenium driver
@fixture
def browser_chrome(context):
    # Set up the driver
    context.driver = setup_driver()

    # Run the tests
    yield context.driver

    # Tear down the driver
    close_driver(context.driver)
