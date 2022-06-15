from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, browser, url, timeout=7):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def open_images_link(self):
        images = self.browser.find_element(*BasePageLocators.IMAGES_LINK)
        images.click()

    def search(self):
        search_box = self.browser.find_element(*BasePageLocators.SEARCH_INPUT_BOX)
        search_box.send_keys(Keys.RETURN)
        
    def type_into_search_box(self):
        search_box = self.browser.find_element(*BasePageLocators.SEARCH_INPUT_BOX)
        search_box.send_keys("Тензор")

    def there_should_be_search_box(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_INPUT_BOX), "Нету строки ввода для поиска"

    def there_should_be_suggestion_fields(self):
        assert self.is_element_present(*BasePageLocators.SUGGEST_AFTER_INPUT_IN_SEARCH_BOX), "Нету полей с " \
                                                                                             "подсказками поиска "

    def there_should_be_images_link(self):
        assert self.is_element_present(*BasePageLocators.IMAGES_LINK)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_value_presented(self, how, what):
        assert self.browser.find_element(how, what).get_attribute("value") != ""

    def handle_stale_element(self, how, what):
        ignored_exceptions = (StaleElementReferenceException,)
        return WebDriverWait(self.browser, 2, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((how, what)))