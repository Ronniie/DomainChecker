from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
                '//*[@id="react-nc-search"]/div/div/section/article/div[1]/h2')[0].text
            return True
        except NoSuchElementException: # Will update this to fit a certain Exception.
            return False

    def premium(self):
        try:
            if self.driver.find_element_by_xpath(
                    '//*[@id="react-nc-search"]/div/div[1]/section/article/div[1]/span').text == "PREMIUM":  # noqa: E501
                return True
        except NoSuchElementException: # Will update this to fit a certain Exception.
            return False

    def logging(self, status="unavailable", price=None):
        if status == "available":
            return f"{settings.colors.SUCCESS}Domain ({self.domain}) is available for {price}!{settings.colors.WHITE}"  # noqa: E501
        elif status == "premium":
            return f"{settings.colors.WARNING}Premium Domain ({self.domain}) is available for {price}!{settings.colors.WHITE}"  # noqa: E501
        elif status == "unavailable":
            return f"{settings.colors.FAIL}Domain ({self.domain}) is unavailable.{settings.colors.WHITE}"  # noqa: E501

    def price(self):
        if self.exists():
            try:
                price = self.driver.find_element_by_xpath(
                    '//*[@id="react-nc-search"]/div/div/section/article/div[2]/strong').text
                if self.premium():
                    return self.logging(status="premium", price=price)
                else:
                    return self.logging(status="available", price=price)
            except NoSuchElementException:
                return self.logging()
        else:
            return self.logging()
