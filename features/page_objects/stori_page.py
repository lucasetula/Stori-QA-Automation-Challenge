from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from features.locators import stori_page_locators
import time


class StoriPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_stori_page(self, url):
        self.driver.get(url)

    def select_country(self, country):
        self.driver.find_element(*stori_page_locators.COUNTRY_INPUT).click()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-1"]')))
            if country == "Mexico":
                self.driver.find_element(*stori_page_locators.COUNTRY_INPUT).send_keys("ME")
                self.driver.find_element(*stori_page_locators.MEXICO_OPTION).click()
            elif country == "United States":
                self.driver.find_element(*stori_page_locators.COUNTRY_INPUT).send_keys("UNI")
                self.driver.find_element(*stori_page_locators.USA_OPTION).click()
            elif country == "United Arab Emirates":
                self.driver.find_element(*stori_page_locators.COUNTRY_INPUT).send_keys("UNI")
                self.driver.find_element(*stori_page_locators.UAE_OPTION).click()
            elif country == "Argentina":
                self.driver.find_element(*stori_page_locators.COUNTRY_INPUT).send_keys("AR")
                self.driver.find_element(*stori_page_locators.ARG_OPTION).click()
            self.driver.find_element(*stori_page_locators.COUNTRY_INPUT).clear()
        except:
            print("The country was not found.")

    def select_options(self, option):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dropdown-class-example"]')))
            if option == "Two":
                self.driver.find_element(*stori_page_locators.OPTIONS_SELECT).click()
                self.driver.find_element(*stori_page_locators.OPTION_2).click()
            elif option == "Three":
                self.driver.find_element(*stori_page_locators.OPTIONS_SELECT).click()
                self.driver.find_element(*stori_page_locators.OPTION_3).click()
            time.sleep(2)
        except:
            print("The option was not found.")

    def open_window(self):
        self.driver.find_element(*stori_page_locators.OPEN_WINDOW).click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(5)
        self.driver.find_element(*stori_page_locators.LOGO).click()
        time.sleep(5)

    def open_tab(self):
        try:
            self.driver.find_element(*stori_page_locators.OPEN_TAB).click()
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[1])
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            self.driver.save_screenshot("Task #5 Switch Tab Example.jpg")
            time.sleep(3)
            self.driver.switch_to.window(window_handles[0])
            time.sleep(2)

        except:
            print("")

    def alert_testing(self):
        self.driver.find_element(*stori_page_locators.ALERT_INPUT).click()
        self.driver.find_element(*stori_page_locators.ALERT_INPUT).send_keys("Stori Card")
        self.driver.find_element(*stori_page_locators.ALERT_BUTTON).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.find_element(*stori_page_locators.ALERT_INPUT).clear()

    def confirm_testing(self):
        self.driver.find_element(*stori_page_locators.ALERT_INPUT).send_keys("Stori Card")
        self.driver.find_element(*stori_page_locators.CONFIRM_BUTTON).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.find_element(*stori_page_locators.ALERT_INPUT).clear()

    def costs(self):
        table = self.driver.find_element(By.CSS_SELECTOR, "#product")
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows[1:]:
            cells = row.find_elements(By.CSS_SELECTOR, "td")
            if len(cells) > 2:
                price = int(cells[2].text)
                if price == 25:
                    course = cells[1].text
                    print(f"Curso: {course}, Precio: {price}")

        self.driver.quit()

    def print_engineers(self):
        engineers = self.driver.find_elements(By.XPATH, "//table[@id='product']//tr[td[2]='Engineer']/td[1]")
        print("Engineers:")
        for engineer in engineers:
            print(engineer.text)

    def print_businessmans(self):
        business = self.driver.find_elements(By.XPATH, "//table[@id='product']//tr[td[2]='Businessman']/td[1]")
        print("Business:")
        for businessman in business:
            print(businessman.text)

    def iframe(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='list-style-two']")
        for element in elements:
            text = element.text.strip()
            if text == stori_page_locators.MENSAJES:
                print(text)
                break
        else:
            print("The element was not found.")