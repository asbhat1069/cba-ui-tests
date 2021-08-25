from .functions import HomePageFunctions


class HomePage(HomePageFunctions):
    def __init__(self, web_driver):
        HomePageFunctions.__init__(self, web_driver)