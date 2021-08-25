from .page_objects import HomePageObjects
from constants import WaitTime


class HomePageWebElements:
    def __init__(self, web_driver):
        self._web_driver = web_driver

    def username_input(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_css(
            HomePageObjects.username_input, timeout
        )

    def create_warrior_button(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_css(
            HomePageObjects.create_warrior_button, timeout
        )

    def start_journey_button(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_css(
            HomePageObjects.start_journey_button, timeout
        )

    def start_journey_button_with_name(self, name, timeout=WaitTime.S):
        return self._web_driver.get_element_by_xpath(
            HomePageObjects.start_journey_button_with_name.format(name), timeout
        )
