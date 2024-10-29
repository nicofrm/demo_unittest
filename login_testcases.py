from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
import time

class Login_page_verification(unittest.TestCase):
    LINK = "https://magento.softwaretestingboard.com/"
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign In")
    SIGN_IN_BUTTON = (By.XPATH,'//button[@class="action login primary"]')
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create an Account")
    REQUIRED_FIELD_ERROR = (By.XPATH, '//*[@class="input-text mage-error"]//following-sibling::div')
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = ( By.NAME, "lastname")
    EMAIL_LOGIN = (By.XPATH, '//input[@title="Email"]')
    EMAIL = (By.XPATH, '//input[@autocomplete="email"]')
    PASSWORD = (By.ID, 'pass')
    PASSWORD1 = (By.ID, "password")
    PASSWORD2 = (By.ID, "password-confirmation")
    CREATE_BUTTON = (By.XPATH,'//button[@class="action submit primary"]')
    LOGIN_MESSAGE = (By.LINK_TEXT, 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.LINK)
        self.driver.find_element(*self.SIGN_IN_LINK).click()

    def tearDown(self) -> None:
        self.driver.close()

    def test_signin_link_is_displayed(self):
        sign_in_link = self.driver.find_element(*self.SIGN_IN_LINK)
        assert sign_in_link.is_displayed(), "Sign in link is not displayed on main paige"

    def test_login_button_is_displayed(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()
        sign_in_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        assert sign_in_button.is_displayed()

    def test_login_empty_user_pass(self):
        time.sleep(5)
        sign_in_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.click()

        required_field_errors = self.driver.find_elements(*self.REQUIRED_FIELD_ERROR)
        is_error_message_correct = True
        for i in range(len(required_field_errors)):
            if required_field_errors[i].text != 'This is a required field.':
                is_error_message_correct = False
        assert sign_in_button.is_displayed() == True, f"Error: The login was done without credentials"
        assert is_error_message_correct == True, f"Error, at least one field is not marked as required"

    def test_create_username_and_password(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_LINK).click()
        time.sleep(2)
        self.driver.find_element(*self.FIRST_NAME).send_keys("Nicoleta")
        self.driver.find_element(*self.LAST_NAME).send_keys("Frumosu")
        time.sleep(2)
        self.driver.find_element(*self.EMAIL).send_keys("nicoleta.frumosu12@gmail.com")
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD1).send_keys("Nicoleta1")
        self.driver.find_element(*self.PASSWORD2).send_keys("Nicoleta1")
        time.sleep(2)
        self.driver.find_element(*self.CREATE_BUTTON).click()
        time.sleep(2)

    def test_invalid_user_pass(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()
        self.driver.find_element(*self.EMAIL_LOGIN).send_keys("nicoletafrumosu@ymail.com")
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD).send_keys("Nicoleta1")
        expected_text = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
        actual_text = self.driver.find_element(*self.LOGIN_MESSAGE).text
        assert expected_text == actual_text, f"ERROR AT LOGIN"


    def test_create_valid_user_pass(self):
        pass

    def test_invalid_user_valid_pass(self):
        pass

    def test_valid_user_invalid_pass(self):
        pass

    def test_verify_account_exists(self):
        pass

