from selenium import webdriver
import settings
import time


class Resolver:
    def __init__(self, domain):
        self.domain = domain
        self.api_url = f"{settings.API_URL}{domain}"
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.binary_location = settings.BINARY_LOCATION
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.api_url)
        time.sleep(6)

    def exists(self):
        try:
            self.driver.find_elements_by_xpath(
                '//*[@id="search-results"]/article[1]/div[2]/strong')[0].text
            return True
        except Exception: # Will update this to fit a certain Exception.
            return False

    def premium(self):
        try:
            if self.driver.find_element_by_xpath(
                    '//*[@id="react-nc-search"]/div/div[1]/section/article/div[1]/span').text == "PREMIUM":  # noqa: E501
                return True
        except Exception: # Will update this to fit a certain Exception.
            return False

    def price(self):
        if self.exists():
            price = self.driver.find_element_by_xpath(
                '//*[@id="search-results"]/article[1]/div[2]/strong').text
            if self.premium():
                return f"{settings.colors.WARNING}Premium Domain ({self.domain}) is available for {price}!{settings.colors.WHITE}"  # noqa: E501
            else:
                return f"{settings.colors.SUCCESS}Domain ({self.domain}) is available for {price}!{settings.colors.WHITE}"  # noqa: E501
        else:
            return f"{settings.colors.FAIL}Domain ({self.domain}) is unavailable.{settings.colors.WHITE}"  # noqa: E501
