from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import robot.api.logger as logger
import time
from constants import WaitTime


class WebElements:
    def __init__(self, driver):
        self._driver = driver

    def open(self, path):
        logger.info(f"Launching url : {path}")
        self._driver.get(path)

    def quit(self):
        self._driver.quit()

    def close_window(self):
        self._driver.close()

    def refresh_page(self):
        logger.info("refreshing browser page")
        self._driver.refresh()

    def scroll_to_desired_element(self, elm, allign_to_top=False):
        self._driver.execute_script(
            "arguments[0].scrollIntoView(arguments[1]);", elm, allign_to_top
        )
        time.sleep(WaitTime.XXS)

    def accept_alert_popup(self):
        self._driver.switch_to.alert.accept()

    def wait_until_presence_of_element(self, by_selector, identifier, timeout=WaitTime.S):
        return WebDriverWait(self._driver, timeout, timeout / 6).until(
            EC.presence_of_element_located((by_selector, identifier)),
            message=f"No element found for selector '{by_selector}' and identifier '{identifier}'",
        )

    def wait_until_visibility_of_element(self, by_selector, identifier, timeout=WaitTime.S):
        return WebDriverWait(self._driver, timeout, timeout / 6).until(
            EC.visibility_of_element_located((by_selector, identifier)),
            message=f"No element found for selector '{by_selector}' and identifier '{identifier}'",
        )

    def wait_until_invisibility_of_element(self, by_selector, identifier, timeout=WaitTime.S):
        return WebDriverWait(self._driver, timeout, timeout / 6).until(
            EC.invisibility_of_element_located((by_selector, identifier)),
            message=f"Element still visible for selector '{by_selector}' and identifier '{identifier}'",
        )

    def wait_until_element_is_clickable(self, by_selector, identifier, timeout=WaitTime.S):
        return WebDriverWait(self._driver, timeout, timeout / 6).until(
            EC.element_to_be_clickable((by_selector, identifier)),
            message=f"Element not clickable yet for '{by_selector}' and identifier '{identifier}'",
        )

    def get_element_by_xpath(self, xpath, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(By.XPATH, xpath, timeout)

    def get_element_by_css(self, css_selector, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(
            By.CSS_SELECTOR, css_selector, timeout
        )

    def get_element_by_link_text(self, link_text, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(
            By.PARTIAL_LINK_TEXT, link_text, timeout
        )

    def get_element_by_class_name(self, class_name, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(By.CLASS_NAME, class_name, timeout)

    def get_element_by_id(self, id_text, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(By.ID, id_text, timeout)

    def get_element_by_name(self, name, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(By.NAME, name, timeout)

    def get_elements_by_tag_name(self, tag_name, timeout=WaitTime.S):
        return self.wait_until_presence_of_element(By.TAG_NAME, tag_name, timeout)
