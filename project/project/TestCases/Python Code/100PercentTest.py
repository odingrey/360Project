# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 100PercentTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev.sodaasu.com/slowergram"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_100_percent(self):
        driver = self.driver
        driver.get(self.base_url + "/slowergram")
        driver.find_element_by_link_text("Michael Sprague-Eckenrode").click()
        driver.get(self.base_url + "/slowergram")
        driver.find_element_by_link_text("Cory Calhoun").click()
        driver.get(self.base_url + "/slowergram")
        driver.find_element_by_link_text("Tyler Brockett").click()
        driver.get(self.base_url + "/slowergram")
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("ron4@yahoo.com")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("ron")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("ron")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("rob1@yahoo.com")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("ron")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("ron")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Return to the homepage.").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("rob1@yahoo.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("ron")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("img.button.img-circle").click()
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_id("id_picture").clear()
        driver.find_element_by_id("id_picture").send_keys("/var/www/slowergram/project/project/static/images/AI_Logo_PNG-300x145.png")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Picture1")
        driver.find_element_by_id("id_file").clear()
        driver.find_element_by_id("id_file").send_keys("/var/www/slowergram/project/project/static/images/AI_Logo_PNG-300x145.png")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("Picture1").click()
        driver.find_element_by_id("brightness_slider").clear()
        driver.find_element_by_id("brightness_slider").send_keys("90")
        driver.find_element_by_id("brightness_slider").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_id("Picture1").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "(//button[@type='button'])[4]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("Are you sure you want to delete Picture1", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text("SlowerGram").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Picture1")
        driver.find_element_by_id("id_file").clear()
        driver.find_element_by_id("id_file").send_keys("/var/www/slowergram/project/project/static/images/AI_Logo_PNG-300x145.png")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("a.dropdown-toggle").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
