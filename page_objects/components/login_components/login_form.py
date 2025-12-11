from selenium.webdriver.common.by import By

from page_objects.pages.base_page import BasePage


class LoginForm(BasePage):
    """
    Форма Login
    """
    FIELD_USERNAME_OR_EMAIL = (By.NAME, "username")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_loading(element_locator=self.FIELD_USERNAME_OR_EMAIL)

    # Методи для роботи з елементами
    def enter_credentials(self, username, password):
        self.fill_text(self.FIELD_USERNAME_OR_EMAIL, username)
        self.fill_text(self.FIELD_PASSWORD, password)

    def click_login(self):
        self.click_element(self.BUTTON_LOGIN)
