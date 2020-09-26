# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://selenium1py.pythonanywhere.com/ru/")
        driver.find_element_by_id("login_link").click()
        driver.find_element_by_id("id_registration-email").click()
        driver.find_element_by_id("id_registration-email").clear()
        driver.find_element_by_id("id_registration-email").send_keys("agfgadfdg@test.com")
        driver.find_element_by_id("id_registration-password1").click()
        driver.find_element_by_id("id_registration-password1").clear()
        driver.find_element_by_id("id_registration-password1").send_keys("QqWwEe!1@2")
        driver.find_element_by_id("id_registration-password2").click()
        driver.find_element_by_id("id_registration-password2").clear()
        driver.find_element_by_id("id_registration-password2").send_keys("QqWwEe!1@2")
        driver.find_element_by_name("registration_submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()