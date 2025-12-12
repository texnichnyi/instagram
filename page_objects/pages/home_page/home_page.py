from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from page_objects.components.home_components.post_component import PostComponent
from page_objects.pages.base_auth_page import BaseAuthPage


class HomePage(BaseAuthPage):
    """
    Cторінка Home. Фактично головна сторінка користувача
    """
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search']")
    NOTIFICATION_BUTTON = (By.CSS_SELECTOR, "a[href='/notifications/']")
    ALL_POSTS = (By.CSS_SELECTOR, "article")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_loading(element_locator=self.NOTIFICATION_BUTTON)

    def get_all_posts(self) -> list[PostComponent]:
        post_elements = self.find_elements(self.ALL_POSTS)
        post_objects = []
        for element in post_elements:
            post_objects.append(PostComponent(self.driver, element))

        return post_objects

    def get_post_by_author(self, post_author: str) -> PostComponent:
        specific_post = (By.XPATH, f"//span[text()='{post_author}']/ancestor::article")
        try:
            root_element = self.find_element(specific_post)
            return PostComponent(self.driver, root_element)
        except TimeoutException:
            raise NoSuchElementException(f"Пост автора '{post_author}' не знайдено.")

    def scroll_feed_to_bottom(self) -> bool:
        target_locator = self.footer.LINK_META
        return self.scroll_to_element(target_locator)
