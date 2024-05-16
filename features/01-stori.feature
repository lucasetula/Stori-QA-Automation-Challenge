@fixture(browser_chrome)
Feature: Story QA Challenge

  @stori1 @stori
  Scenario: Task #1 Open browser
    Given the QA Engineer is on the base page

  @stori2 @stori
  Scenario: Task #2 Select Countries
    Given the QA Engineer is on the base page
    When select Mexico
    And select United States
    And select United Arab Emirates
    Then select Argentina

  @stori3 @stori
  Scenario: Task #3 Select Options
    Given the QA Engineer is on the base page
    When select the option two
    And select the option three

  @stori4 @stori
  Scenario: Task #4 Switch Window Example
    Given the QA Engineer is on the base page
    When click on the Open Window button and verify the guarantee message

  @stori5 @stori
  Scenario: Task #5 Switch Tab Example
    Given the QA Engineer is on the base page
    When click on the Open Tab button and scrolling

  @stori6 @stori
  Scenario: Task #6 Switch Alert Example
    Given the QA Engineer is on the base page
    When test the alert

  @stori7 @stori
  Scenario: Task #7 Web Table Example
    Given the QA Engineer is on the base page
    When verify cost

  @stori8 @stori
  Scenario: Task #8 Engineers and businessman
    Given the QA Engineer is on the base page
    When verify engineers
    And verify businessman


  @stori9 @stori
  Scenario: Task #9 Iframe
    Given the QA Engineer is on the base page
    When verify iframe