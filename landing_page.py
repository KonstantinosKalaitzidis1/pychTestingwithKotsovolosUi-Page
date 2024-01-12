# landing_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoAlertPresentException, ElementClickInterceptedException, StaleElementReferenceException
import time

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        self.driver.get("https://www.kotsovolos.gr/?gad_source=1&gclid=CjwKCAiA44OtBhAOEiwAj4gpObAifkPJzXe_PbIEcmOxoD4_WzAdQOxZFNmxGcuQWGhUr2swaUBtPRoCkSQQAvD_BwE")

    def wait_for_element_visibility(self, by, value, timeout=100):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException as e:
            if isinstance(e, WebDriverException):
                try:
                    alert = self.driver.switch_to.alert
                    alert.dismiss()
                    self.wait_for_element_visibility(by, value, timeout)
                except NoAlertPresentException:
                    pass
            else:
                raise TimeoutException(f"Timed out waiting for element {by}: {value} to be visible. {str(e)}")

    def click_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 300).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            # Handle click interception or stale element reference
            time.sleep(1)
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
