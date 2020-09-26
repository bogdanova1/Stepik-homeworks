

def search_item(browser, search_text):
    browser.find_element_by_css_selector("input[type = 'search']").send_keys(search_text)
    browser.find_element_by_css_selector('.navbar-form.navbar-right input[type = "submit"]').click()