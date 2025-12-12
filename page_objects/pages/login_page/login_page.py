from page_objects.components.login_components.login_form import LoginForm
from page_objects.pages.base_unathorized_page import BaseUnathorizedPage
from page_objects.pages.home_page.home_page import HomePage


class LoginPage(BaseUnathorizedPage):
    """
    Cторінка Login
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.login_form = LoginForm(self.driver)

    def login(self, username, password):
        self.login_form.enter_credentials(username, password)
        self.login_form.click_login()
        return HomePage(self.driver)
