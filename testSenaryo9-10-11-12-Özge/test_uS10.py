# Generated by Selenium IDE
import pytest
import allure
from Locator.constant import *
from helpers import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUS10:
    
    EMAIL = "ozgecam@outlook.com"
    PASSWORD = "ozgecam-pair2"
    SECOND = 20

    def setUP(self, method):
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

    @allure.title("Kullanıcı, değerlendirmeler sayfasını görüntüleyebilmelidir")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS10TC1(self, email, password):
        self.login_Call(email, password)
        assert "Değerlendirmeler" in self.driver.title, "Değerlendirmeler sayfası yüklenemedi."

    @allure.title("Kullanıcı, değerlendirmeler alanından kişisel analiz raporlarını görüntüleyebilmelidir")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS10TC2(self, email, password):
        self.login_Call(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((VIEW_REPORT_LOCATOR))).click()
        new_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/degerlendirmeler/rapor/tobeto-iste-basari-modeli/1"
        assert new_url == expected_url, "Sayfa görüntülenemedi."


    @allure.title("Kullanıcı, çoktan seçmeli test raporlarını görüntüleyebilmelidir")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS10TC3(self, email, password):
        self.login_Call(email, password)
        self.driver.execute_script("window.scrollTo(0, 400)")
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((FRONT_REPORT_ONE))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((FRONT_REPORT_TWO))).click()
        assert WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((TEST_BITTI))).text == "Test Bitti"




    
