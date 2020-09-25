import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                     help="Choose language for tests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("--language should be chose")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages: language'})

    print("\nopen browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    yield browser

    print("\nquit browser..")
    browser.quit()
