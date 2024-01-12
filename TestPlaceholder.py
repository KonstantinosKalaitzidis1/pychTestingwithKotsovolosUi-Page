# test_placeholder.py

import pytest
from landing_page import LandingPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_teardown")
class TestPlaceholder:

    def test_search_placeholder(self, setup_teardown):
        landing_page = LandingPage(setup_teardown)


        landing_page.navigate_to_page()


        search_input_locator = (By.XPATH, "//*[@id='searchTermSN']")


        landing_page.wait_for_element_visibility(*search_input_locator)


        search_input = landing_page.driver.find_element(*search_input_locator)


        placeholder_text = search_input.get_attribute("placeholder")



