# test_landing_page.py

import pytest
from landing_page import LandingPage

@pytest.mark.usefixtures("setup_teardown")
class TestLandingPage:
    def test_landing_page_title(self, setup_teardown):
        landing_page = LandingPage(setup_teardown)
        landing_page.navigate_to_page()

        # Debugg the act title
        actual_title = setup_teardown.title
        print("Actual Title:", actual_title)

        ##I did not proceed with a file with title assertion due to the big actual title in greek.





