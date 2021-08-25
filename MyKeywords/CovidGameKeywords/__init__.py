from MyKeywords.infra.web_driver_manager import WebDriverManager
from MyKeywords.infra.web_elements import WebElements
from .HomePage import HomePage
from .Challenges import Challenges


class CovidGameKeywords(HomePage, Challenges):
    def __init__(self, browser, headless=False,responsive=False, device_name="iPhone X"):
        _driver = WebDriverManager.get_web_driver(
            browser,
            headless=headless,
            responsive=responsive,
            device_name=device_name,
        )
        self._web_driver = WebElements(_driver)
        HomePage.__init__(self, self._web_driver)
        Challenges.__init__(self, self._web_driver)
