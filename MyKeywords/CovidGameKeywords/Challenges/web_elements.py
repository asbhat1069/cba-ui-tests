from .page_objects import ChallengePageObjects
from constants import WaitTime
from selenium.webdriver.common.by import By


class ChallengeWebElements:
    def __init__(self, web_driver):
        self._web_driver = web_driver

    def game_header(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_xpath(
            ChallengePageObjects.game_header, timeout
        )

    def battlefield_challenge_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.battlefield_challenge_button, timeout
        )

    def bus_challenge_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.bus_challenge_button, timeout
        )

    def start_battlefield_challenge_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.start_battlefield_challenge_button, timeout
        )

    def start_bus_challenge_timer(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.bus_timer_start, timeout
        )

    def continue_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.continue_button, timeout
        )

    def answer_link(self, answer, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.XPATH,  ChallengePageObjects.answer_link.format(answer.lower()), timeout
        )

    def correct_answer_header(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_xpath(
            ChallengePageObjects.correct_answer_header, timeout
        )

    def wrong_answer_header(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_xpath(
            ChallengePageObjects.wrong_answer_header, timeout
        )

    def try_again_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.XPATH, ChallengePageObjects.try_again_button, timeout
        )

    def leaderboard_header(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_xpath(
            ChallengePageObjects.leaderboard_header, timeout
        )

    def continue_fighting_button(self,timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.continue_fighting_button, timeout
        )

    def try_next_battle_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.try_next_battle_button, timeout
        )

    def check_final_score_button(self, timeout=WaitTime.S):
        return self._web_driver.wait_until_element_is_clickable(
            By.CSS_SELECTOR, ChallengePageObjects.check_final_score_button, timeout
        )

    def start_challenge_button(self, timeout=WaitTime.S):
        return self._web_driver.get_element_by_xpath(
            ChallengePageObjects.start_challenge_button, timeout
        )


