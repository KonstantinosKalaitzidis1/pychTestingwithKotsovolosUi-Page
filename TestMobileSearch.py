# test_mobile_option.py

import pytest
from landing_page import LandingPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
class TestMobileOption:

    def test_choose_mobile_option(self, setup_teardown):
        landing_page = LandingPage(setup_teardown)


        landing_page.navigate_to_page()


        search_input_locator = (By.XPATH, "//*[@id='searchTermSN']")


        landing_page.wait_for_element_visibility(*search_input_locator)


        search_input = landing_page.driver.find_element(*search_input_locator)


        search_input.send_keys("mob")


        dropdown_css_selector = "div.autocomplete-suggestions"
        landing_page.wait_for_element_visibility(By.CSS_SELECTOR, dropdown_css_selector)

        landing_page.click_element(By.XPATH,"//*[@id='searchBoxSN']/span/span/div/div/div/div[1]/div/ul/li[1]/a")

        landing_page.click_element(By.XPATH, '//*[@id="Layer_1"]')




