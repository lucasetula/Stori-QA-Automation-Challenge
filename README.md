# Stori-QA-Automation-Challenge
A framework for UI automation using Selenium and Behave.

## Project Structure
- **config:** Configuration settings for the project.
  - **config/config.py:** Stores variables used across the entire project, like URLs or database connections,
  or to store global settings encapsulated in one place.
  - **config/driver_setup.py:** Manages the creation, setup and tear down of the WebDriver
  - **features/steps/stori_steps.py:** Manages configurations specific to Behave, like fixtures or the treatment of scenarios,
  steps, etc.
- **features:** Contains your Gherkin feature files.
  - **features/environment.py:** Behave environment setup. Set up hooks like before_all, before_scenario, etc.
- **utils:** Utility modules and helper functions.

## Run Locally
Clone the project

```bash
  install python 3.12
  configure Python Interpreter
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the tests

```bash
  behave --tags=@stori
  behave --format allure_behave.formatter:AllureFormatter -o Reports
```

Run the single tests

```bash
  behave --tags=@stori1
  e.g behave --tags=@stori2
```