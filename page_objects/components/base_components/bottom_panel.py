from selenium.webdriver.common.by import By

from page_objects.pages.base_auth_page import BaseAuthPage


class BottomPanel(BaseAuthPage):
    """
    Нижня панель, доступна всюди для залогованих користувачів
    """
    MESSAGES_BUTTON = (By.XPATH, "(//*[local-name()='svg' and @aria-label='Messages'])[1]")
    HOME_BUTTON = (By.CSS_SELECTOR, "svg[aria-label='Home']")
    EXPLORE_BUTTON = (By.CSS_SELECTOR, "svg[aria-label='Explore']")
    REELS_BUTTON = (By.CSS_SELECTOR, "svg[aria-label='Reels']")
    NEW_POST_BUTTON = (By.CSS_SELECTOR, "svg[aria-label='New post']")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "img[alt='profile picture']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_loading(element_locator=self.HOME_BUTTON)