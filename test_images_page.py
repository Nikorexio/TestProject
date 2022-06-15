from .page.base_page import BasePage
from .page.popular_image_categories_page import PopularImagesPage
from .page.chosen_images_category_page import ChosenImageCategoryPage, image_should_be_switched, image_should_be_same


def test_second_part(browser):
    link = "https://yandex.ru/"
    page = BasePage(browser, link)
    page.open()
    page.there_should_be_images_link()
    page.open_images_link()
    popular_images_page = PopularImagesPage(browser, browser.switch_to.window(browser.window_handles[1]))
    popular_images_page.current_url_should_be_equal_to_given_url()
    popular_images_page.open_first_category_of_images()
    chosen_image_page = ChosenImageCategoryPage(browser, browser.current_url)
    chosen_image_page.there_should_be_name_of_chosen_category()
    chosen_image_page.open_first_image_item()
    chosen_image_page.image_should_open()
    first_image = chosen_image_page.take_current_image_data()
    chosen_image_page.switch_to_next_picture()
    second_image = chosen_image_page.take_current_image_data()
    image_should_be_switched(first_image, second_image)
    chosen_image_page.switch_to_previous_picture()
    current_image = chosen_image_page.take_current_image_data()
    image_should_be_same(first_image, current_image)
