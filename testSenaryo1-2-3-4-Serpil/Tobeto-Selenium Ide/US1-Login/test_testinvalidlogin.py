# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestinvalidlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testinvalidlogin(self):
    self.driver.get("https://tobeto.com/giris")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("invalid@gmail.com")
    self.driver.find_element(By.NAME, "password").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".d-none > .nav-item:nth-child(4) > .nav-link")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "password").send_keys("wrongpassword")
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".mt-4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Geçersiz e-posta veya şifre."
  
