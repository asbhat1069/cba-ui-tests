from .web_elements import ChallengeWebElements
from constants import WaitTime
import robot.api.logger as logger


class ChallengeFunctions:
    def __init__(self, web_driver):
        self._web_driver = web_driver
        self.challenge = ChallengeWebElements(self._web_driver)

    def start_battlefield_challenge(self):
        self.challenge.game_header(WaitTime.M)
        logger.info("Selecting news challenge")

        challenge_button = self.challenge.battlefield_challenge_button(WaitTime.M)
        self._web_driver.scroll_to_desired_element(challenge_button, allign_to_top=False)
        challenge_button.click()

        logger.info("starting challenge")
        self.challenge.start_battlefield_challenge_button(WaitTime.M).click()

    def start_bus_challenge(self):
        self.challenge.game_header(WaitTime.M)
        logger.info("Selecting Bus challenge")

        bus_challenge = self.challenge.bus_challenge_button(WaitTime.M)
        self._web_driver.scroll_to_desired_element(bus_challenge, allign_to_top=False)
        bus_challenge.click()

        logger.info("starting challenge")
        self.challenge.start_bus_challenge_timer(WaitTime.M).click()

    def select_answer(self, answer):
        logger.info(f"Clicking answer: {answer}")
        self.challenge.answer_link(answer, WaitTime.M).click()

    def continue_on_correct_answer(self):
        self.challenge.correct_answer_header(WaitTime.M)
        self.challenge.continue_button().click()

    def try_again_on_wrong_answer(self):
        self.challenge.wrong_answer_header(WaitTime.M)
        self.challenge.try_again_button().click()

    def try_next_challenge(self):
        self.challenge.try_next_battle_button(WaitTime.M).click()
        self.challenge.start_challenge_button(WaitTime.M)

    def check_leaderboard_for_final_score(self):
        self.challenge.check_final_score_button(WaitTime.M).click()

    def click_continue_fighting_on_leaderboard(self):
        self.challenge.leaderboard_header(WaitTime.M)
        self.challenge.continue_fighting_button(WaitTime.M).click()

