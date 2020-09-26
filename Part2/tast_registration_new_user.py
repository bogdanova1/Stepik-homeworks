import random
import string


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

def test_registration_new_user(browser):
    def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

    password = random_string("", 9)
    email = password + "@test.com"

    # Arrange
    browser.get(main_page_link)

    # Act
    browser.find_element_by_id("login_link").click()
    browser.find_element_by_id("id_registration-email").send_keys(email)
    browser.find_element_by_id("id_registration-password1").send_keys(password)
    browser.find_element_by_id("id_registration-password2").send_keys(password)
    browser.find_element_by_css_selector("button[name = 'registration_submit']").click()

    # Assert
    message = browser.find_element_by_class_name("alertinner")
    assert "Спасибо за регистрацию!" in message.text, "No message about registration"

