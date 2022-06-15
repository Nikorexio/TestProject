from .page.base_page import BasePage
from .page.search_result_page import SearchResultPage


def test_first_part(browser):
    link = "https://yandex.ru/"
    page = BasePage(browser, link)
    page.open()
    page.there_should_be_search_box()
    page.type_into_search_box()
    page.there_should_be_suggestion_fields()
    page.search()
    search_page = SearchResultPage(browser, browser.current_url)
    search_page.is_there_search_result()
    search_page.should_be_tensor_link()