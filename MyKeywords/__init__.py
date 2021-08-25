from .CovidGameKeywords import CovidGameKeywords
from constants import BROWSER, HEADLESS, RESPONSIVE, DEVICENAME


class MyKeywords(CovidGameKeywords):
    def __init__(
            self,
            browser=BROWSER,
            headless=HEADLESS,
            responsive=RESPONSIVE,
            device_name=DEVICENAME
    ):
        CovidGameKeywords.__init__(
            self,
            browser,
            headless,
            responsive,
            device_name
        )

    def open(self, path):
        self._web_driver.open(path)

    def close_all(self):
        self._web_driver.quit()
