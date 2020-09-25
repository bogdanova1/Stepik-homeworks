#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
main_page_link = "http://selenium1py.pythonanywhere.com/"


def test_search_article(browser):
    search_name = "The shellcoder's handbook"

    # Arrange
    browser.get(main_page_link)

    # Act
    browser.find_element_by_css_selector("input[type = 'search']").send_keys(search_name)
    browser.find_element_by_css_selector('.navbar-form.navbar-right input[type = "submit"]').click()

    # Assert
    title_text = browser.find_element_by_class_name('page-header').text
    assert search_name in title_text, \
        "Page title '%s' should contain search text '%s'" % (title_text, search_name)
    articles = browser.find_elements_by_css_selector(".product_pod")
    for article in articles:
        assert search_name.upper() in article.find_element_by_css_selector("h3 a").text.upper(), \
            "Article name '%s' should contain search text '%s'" % (search_name, article.text)
        assert search_name.upper() in article.find_element_by_css_selector("img").get_attribute("alt").upper(), \
            "Article image '%s' should contain search text '%s'" % (search_name, article.text)

