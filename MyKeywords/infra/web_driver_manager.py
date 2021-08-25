from selenium import webdriver
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener,
)
from robot.libraries.Screenshot import Screenshot
from constants import SCREENSHOT_DIR
import shortuuid
import os


class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_path = os.path.join(
            SCREENSHOT_DIR, f"screenshot_{shortuuid.uuid()}.png"
        )
        driver.save_screenshot(screenshot_path)
        Screenshot()._embed_screenshot(screenshot_path, width="200px")


class WebDriverManager(object):

    __driver = None

    @classmethod
    def get_web_driver(
        cls, browser, headless=False, responsive=False, device_name="iPhone X"
    ):
        if cls.__driver is None:
            if browser.lower() == "chrome":
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--incognito")
                if headless:
                    chrome_options.add_argument("--no-sandbox")
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--disable-dev-shm-usage")
                    chrome_options.add_argument('--disable-gpu')
                if headless and not responsive:
                    chrome_options.add_argument("--window-size=1920x1080")
                if responsive:
                    mobile_emulation = {"deviceName": device_name}
                    chrome_options.add_experimental_option(
                        "mobileEmulation", mobile_emulation
                    )
                cls.__driver = webdriver.Chrome(
                    desired_capabilities=chrome_options.to_capabilities()
                )
            elif browser.lower() == "firefox":
                cls.__driver = webdriver.Firefox()
            elif browser.lower() == "ie":
                cls.__driver = webdriver.Ie()
            elif browser.lower() == "edge":
                cls.__driver = webdriver.Edge()
        cls.__driver.delete_all_cookies()

        if not responsive and browser.lower() != "ie":
            cls.__driver.maximize_window()
        _event_driver = EventFiringWebDriver(cls.__driver, MyListener())
        return _event_driver
