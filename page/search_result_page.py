from .base_page import BasePage
from .locators import SearchResultPageLocators


class SearchResultPage(BasePage):
    def is_there_search_result(self):
        assert self.is_element_present(*SearchResultPageLocators.TABLE_WITH_SEARCH_RESULTS), "Отсутствуют результаты" \
                                                                                             " поиска"

    def should_be_tensor_link(self):
        assert self.is_element_present(*SearchResultPageLocators.TENSOR_LINK), "В первом элементе результатов поиска" \
                                                                               " нет ссылки на сайт Тензора"
