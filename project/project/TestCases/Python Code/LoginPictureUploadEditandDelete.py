# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginPictureUploadEditandDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev.sodaasu.com/slowergram"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_picture_upload_editand_delete(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.get(self.base_url + "/slowergram")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "id_username"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("cory@yahoo.com")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "id_password"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("cory")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "id_file"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("id_file").clear()
        driver.find_element_by_id("id_file").send_keys("/var/www/slowergram/project/project/static/images/AI_Logo_PNG-300x145.png")
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("picture3")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("picture3").click()
        driver.find_element_by_id("brightness_slider").clear()
        driver.find_element_by_id("brightness_slider").send_keys("44")
        driver.find_element_by_id("brightness_slider").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_id("picture3").click()
        driver.find_element_by_id("brightness_slider").clear()
        driver.find_element_by_id("brightness_slider").send_keys("-38")
        driver.find_element_by_id("brightness_slider").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_id("picture3").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        self.assertEqual("Are you sure you want to delete picture3", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text("SlowerGram").click()
        driver.find_element_by_css_selector("a.dropdown-toggle").click()
        driver.find_element_by_link_text("Logout").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    
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
