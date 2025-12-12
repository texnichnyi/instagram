from selenium.webdriver.common.by import By

from page_objects.pages.base_page import BasePage


class Footer(BasePage):
    """
    Нижній футер, який буде доступний у всіх сторінках
    """
    LINK_META = (By.XPATH, "//footer//a[contains(., 'Meta')]")
    LINK_ABOUT = (By.XPATH, "//footer//a[contains(., 'About')]")
    LINK_BLOG = (By.XPATH, "//footer//a[contains(., 'Blog')]")
    LINK_JOBS = (By.XPATH, "//footer//a[contains(., 'Jobs')]")
    LINK_HELP = (By.XPATH, "//footer//a[contains(., 'Help')]")
    LINK_API = (By.XPATH, "//footer//a[contains(., 'API')]")
    LINK_PRIVACY = (By.XPATH, "//footer//a[contains(., 'Privacy')]")
    LINK_COOKIE_SETTINGS = (By.XPATH, "//footer//a[contains(., 'Cookie Settings')]")
    LINK_TERMS = (By.XPATH, "//footer//a[contains(., 'Terms')]")
    LINK_LOCATIONS = (By.XPATH, "//footer//a[contains(., 'Locations')]")
    LINK_INSTAGRAM_LITE = (By.XPATH, "//footer//a[contains(., 'Instagram Lite')]")
    LINK_THREADS = (By.XPATH, "//footer//a[contains(., 'Threads')]")
    LINK_META_VERIFIED = (By.XPATH, "//footer//a[contains(., 'Meta Verified')]")
    TEXT_COPYRIGHT = (By.XPATH, "(//footer//div[contains(., 'Instagram from Meta')])[last()]")

    def __init__(self, driver):
        super().__init__(driver)

    # Методи для роботи з елементами
    def click_privacy_link(self):
        self.click_element(self.LINK_PRIVACY)
