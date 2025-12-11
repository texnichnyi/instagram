from page_objects.components.sign_up_components.sign_up_form import SignUpForm
from page_objects.pages.home_page.home_page import HomePage


class SignUpPage:
    """
    Cторінка Sign Up
    """
    def __init__(self, driver):
        self.driver = driver
        self.sign_up_form = SignUpForm(self.driver)

    def sign_up_new_user(self, email_or_phone, full_name, username, password):
        self.sign_up_form.enter_registration_data(email_or_phone, full_name, username, password)
        self.sign_up_form.click_sign_up()
        return True # уявимо що ми успішно перенеслись на BirthdayForm
