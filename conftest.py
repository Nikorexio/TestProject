import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Google Chrome(введите --browser_name=chrome)/Firefox(--browser_name=firefox)")


@pytest.fixture(scope="function")
def browser(request):
    web_browser = request.config.getoption("browser_name")
    if web_browser == "chrome":
        browser = webdriver.Chrome()
    elif web_browser == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name=chrome/firefox should be typed")
    yield browser
    print("\nquit browser...")
    browser.quit()
