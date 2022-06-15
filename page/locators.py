from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_INPUT_BOX = (By.CSS_SELECTOR, ".input__box > .input__control")
    SUGGEST_AFTER_INPUT_IN_SEARCH_BOX = (By.CSS_SELECTOR, ".mini-suggest__popup_visible")
    IMAGES_LINK = (By.CSS_SELECTOR, "[data-id='images']")


class SearchResultPageLocators:
    TABLE_WITH_SEARCH_RESULTS = (By.CSS_SELECTOR, ".main__content #search-result")
    TENSOR_LINK = (By.CSS_SELECTOR, '[data-cid="0"] .i-bem .link[href="https://tensor.ru/"]')


class PopularImagesPageLocators:
    FIRST_CATEGORY_ITEM = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")


class ChosenImageCategoryPageLocators:
    FIRST_PICTURE_ITEM = (By.CSS_SELECTOR, ".serp-item_pos_0 .serp-item__link")
    OPENED_IMAGE_VIEWER = (By.CSS_SELECTOR, ".ImagesViewer-Container")
    SWITCH_NEXT_PICTURE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next .CircleButton-Icon")
    SWITCH_PREV_PICTURE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev .CircleButton-Icon")
    CURRENT_IMAGE_DATA = (By.CSS_SELECTOR, ".MMImage-Origin")