from behave import given, when, then
from config import config
from features.page_objects.stori_page import StoriPage


# region Task #1 Open browser

@given("the QA Engineer is on the base page")
def step_given_user_on_login_page(context):
    context.login_page = StoriPage(context.driver)
    context.login_page.navigate_to_stori_page(config.BASE_URL)

# endregion

# region Task #2 Select Countries

@when("select Mexico")
def step_when_user_enters_valid_credentials(context):
    context.login_page.select_country(config.COUNTRY_ONE)

@when("select United States")
def step_when_user_enters_valid_credentials(context):
    context.login_page.select_country(config.COUNTRY_TWO)

@when("select United Arab Emirates")
def step_when_user_enters_valid_credentials(context):
    context.login_page.select_country(config.COUNTRY_THREE)
@then("select Argentina")
def step_when_user_enters_valid_credentials(context):
    context.login_page.select_country(config.COUNTRY_FOUR)

# endregion

#region Task #3 Select Options

@when("select the option two")
def step_when_user_enters_valid_credentials(context):
    context.login_page.select_options(config.OPTION_TWO)


@when("select the option three")
def step_when_user_enters_valid_credentials(context):
    context.login_page.select_options(config.OPTION_THREE)

#endregion

# region Task #4 Switch Window Example

@when("click on the Open Window button and verify the guarantee message")
def step_when_user_enters_valid_credentials(context):
    context.login_page.open_window()

# endregion

# region Task #5 Switch Tab Example

@when("click on the Open Tab button and scrolling")
def step_when_user_enters_valid_credentials(context):
    context.login_page.open_tab()

# endregion

# region Task #6 Switch Alert Example

@when("test the alert")
def step_when_user_enters_valid_credentials(context):
    context.login_page.alert_testing()
    context.login_page.confirm_testing()

# endregion

# region Task #7 Web Table Example

@when("verify cost")
def step_when_user_enters_valid_credentials(context):
    print(context.login_page.obtener_costos_mayores_a_25())

# endregion

# region Task #8 Engineers and businessman

@when("verify engineers")
def step_when_user_enters_valid_credentials(context):
    print(context.login_page.print_engineers())

@when("verify businessman")
def step_when_user_enters_valid_credentials(context):
    print(context.login_page.print_businessmans())

# endregion

# region Task #9 Iframe

@when("verify iframe")
def step_when_user_enters_valid_credentials(context):
    print(context.login_page.iframe())

# endregion
