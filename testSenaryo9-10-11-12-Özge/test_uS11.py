# Generated by Selenium IDE
import pytest

from selenium import webdriver
from Locator.constant import *
from helpers import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUS11():
    BASE_URL = "https://tobeto.com/giris"
    EMAIL = "ozgecam@outlook.com"
    PASSWORD = "ozgecam-pair2"
    SECOND = 20

    def setUp(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def tearDown(self, method):
        self.driver.quit()

    def login_Call(self, email, password):
        
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((EMAIL_NAME))).send_keys(email)
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((PASSWORD_NAME))).send_keys(password)
        iframe = WebDriverWait(self.driver, self.SECOND).until(EC.presence_of_element_located((RECAPTCHA_IFRAME)))
        self.driver.switch_to.frame(iframe)     
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((RECAPTCHA_CHECKBOX))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((LOGIN_BUTTON_LOCATOR))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((DEGERLENDIRME))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((VIEW_REPORT_LOCATOR))).click()


    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)]) 
    def test_US11_TC1(self, email, password):
        self.login_Call(email, password)
        assert "Tobeto İşte Başarı Modeli" in self.driver.title, "Rapor Görüntülenemedi."


    # Analiz raporunda bulunan yetkinlik özniteliklerinin alt butonla açılması 
    @pytest.mark.parametrize("email, password", [(EMAIL,PASSWORD)]) 
    def test_US11_TC2_1(self, email, password):
        self.login_Call(email, password)
        self.driver.execute_script("window.scrollTo(0,400)")
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((OZNITELIK_ACCORD))).click()
        oznitelik = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable(((OZNITELIK_TEXT))))
        assert oznitelik, "Öznitelik görüntülenmemektedir.."

         
        


 
  
