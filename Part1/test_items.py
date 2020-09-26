from Part1 import utils
main_page_link = "http://selenium1py.pythonanywhere.com/"


def test_add_article_to_cart(browser):
    search_text = "The shellcoder's handbook"

    # Arrange
    browser.get(main_page_link)

    # Act
    utils.search_item(browser, search_text)
    buttons = browser.find_elements_by_css_selector(".product_price button[type = 'submit']")

    # Assert
    assert len(buttons) >0, "Button 'add to cart' should be for the article %s" % (search_text)
