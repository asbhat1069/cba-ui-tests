from .web_elements import HomePageWebElements
from constants import WaitTime
import robot.api.logger as logger


class HomePageFunctions:
    def __init__(self, web_driver):
        self._web_driver = web_driver
        self.homepage = HomePageWebElements(self._web_driver)

    def enter_name_and_create_warrior(self, username):
        logger.info(f"Entering username: {username}")
        username_textbox = self.homepage.username_input()
        self._web_driver.scroll_to_desired_element(username_textbox, allign_to_top=True)
        username_textbox.clear()
        username_textbox.send_keys(username)
        logger.info("Click create warrior button")
        self.homepage.create_warrior_button(WaitTime.M).click()

    def start_challenge_journey(self):
        logger.info("Starting challenge journey")
        self.homepage.start_journey_button(WaitTime.M).click()

    def verify_start_journey_button_with_name(self, name):
        self.homepage.start_journey_button_with_name(name, WaitTime.M)
        logger.info(f"Starting challenge journey with uername {name} seen")


