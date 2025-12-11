from selenium.webdriver.common.by import By

from page_objects.pages.base_page import BasePage


class SignUpForm(BasePage):
    """
    Форма Sign Up
    """
    FIELD_MOBILE_OR_EMAIL = (By.NAME, "emailOrPhone")
    FIELD_FULL_NAME = (By.NAME, "fullName")
    FIELD_USERNAME = (By.NAME, "username")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_SIGN_UP = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_loading(element_locator=self.FIELD_MOBILE_OR_EMAIL)

    # Методи для роботи з елементами
    def enter_registration_data(self, email_or_phone, full_name, username, password):
        self.fill_text(self.FIELD_MOBILE_OR_EMAIL, email_or_phone)
        self.fill_text(self.FIELD_FULL_NAME, full_name)
        self.fill_text(self.FIELD_USERNAME, username)
        self.fill_text(self.FIELD_PASSWORD, password)

    def click_sign_up(self):
        self.click_element(self.BUTTON_SIGN_UP)
