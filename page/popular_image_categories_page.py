from .base_page import BasePage
from .locators import PopularImagesPageLocators


class PopularImagesPage(BasePage):
    def open_first_category_of_images(self):
        elem = self.browser.find_element(*PopularImagesPageLocators.FIRST_CATEGORY_ITEM)
        elem.click()

    def current_url_should_be_equal_to_given_url(self):
        assert "https://yandex.ru/images/" in self.browser.current_url, "Url-ы не совпадают"
