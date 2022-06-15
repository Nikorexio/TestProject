from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ChosenImageCategoryPageLocators


def image_should_be_switched(prev_image, curr_image):
    assert prev_image is not curr_image, "Картинка не переключилась..."


def image_should_be_same(prev_image, curr_image):
    assert prev_image == curr_image, "Что-то пошло не так..."


class ChosenImageCategoryPage(BasePage):
    def there_should_be_name_of_chosen_category(self):
        self.is_value_presented(*BasePageLocators.SEARCH_INPUT_BOX)

    def open_first_image_item(self):
        image = self.handle_stale_element(*ChosenImageCategoryPageLocators.FIRST_PICTURE_ITEM)
        image.click()

    def take_current_image_data(self):
        image = self.browser.find_element(*ChosenImageCategoryPageLocators.CURRENT_IMAGE_DATA).get_attribute("src")
        return image

    def switch_to_next_picture(self):
        button = self.handle_stale_element(*ChosenImageCategoryPageLocators.SWITCH_NEXT_PICTURE_BUTTON)
        button.click()

    def switch_to_previous_picture(self):
        button = self.handle_stale_element(*ChosenImageCategoryPageLocators.SWITCH_PREV_PICTURE_BUTTON)
        button.click()

    def image_should_open(self):
        self.is_element_present(*ChosenImageCategoryPageLocators.OPENED_IMAGE_VIEWER)
