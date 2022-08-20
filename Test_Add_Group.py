# -*- coding: utf-8 -*-
from selenium import webdriver
# Указываем полный путь к geckodriver.exe на вашем ПК.
# driver = webdriver.Firefox()
# driver.get('http://localhost/addressbook/group.php')


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        # self.wd.get('http://localhost/addressbook/group.php')
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        # wd.find_element_by_xpath("//input[@value='Login']").click()
        # wd.find_element_by_xpath("//input[@value='Login']").click()
        # wd.find_element_by_name("user").click()
        wd.find_element("name","user").click()
        wd.find_element("name","user").clear()
        wd.find_element("name","user").send_keys("admin")
        wd.find_element("name","pass").clear()
        wd.find_element("name","pass").send_keys("secret")
        wd.find_element("xpath","//input[@value='Login']").click()
        wd.find_element("link text", "groups").click()
        wd.find_element("xpath","//input[@value='New group']").click()
        wd.find_element("name","group_name").click()
        wd.find_element("name","group_name").clear()
        wd.find_element("name","group_name").send_keys("name1")
        wd.find_element("name","group_header").click()
        wd.find_element("name","group_header").clear()
        wd.find_element("name","group_header").send_keys("onn")
        wd.find_element("name","group_footer").click()
        wd.find_element("name","group_footer").clear()
        wd.find_element("name","group_footer").send_keys("ijbjk")
        wd.find_element("xpath","//input[@value='Enter information']").click()
        wd.find_element("link text","group page").click()
        wd.find_element("link text","Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
   
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
