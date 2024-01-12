

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def setup_teardown():

    driver = webdriver.Chrome()
    yield driver


    driver.quit()
