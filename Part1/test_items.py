from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import sys
import traceback

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
main_page_link = "http://selenium1py.pythonanywhere.com/ru/"


def test_search_article():
    part_name = "The shellcoder's handbook"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        browser.find_element_by_css_selector("input[type = 'search']").send_keys(part_name)
        browser.find_element_by_css_selector('.navbar-form.navbar-right input[type = "submit"]').click()

        # Assert
        title_text = browser.find_element_by_class_name('page-header').text
        assert part_name in title_text, \
            "Page title '%s' should contain search text '%s'" % (title_text, part_name)
        articles = browser.find_elements_by_css_selector(".product_pod")
        for article in articles:
            assert part_name.upper() in article.find_element_by_css_selector("h3 a").text.upper(), \
                "Article name '%s' should contain search text '%s'" % (part_name, article.text)
            assert part_name.upper() in article.find_element_by_css_selector("img").get_attribute("alt").upper(), \
                "Article image '%s' should contain search text '%s'" % (part_name, article.text)

    finally:
        browser.quit()
