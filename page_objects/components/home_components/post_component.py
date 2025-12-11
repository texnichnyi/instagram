from selenium.webdriver.common.by import By

from page_objects.pages.base_page import BasePage


class PostComponent(BasePage):
    LIKE_BUTTON = (By.XPATH, ".//*[local-name()='svg' and contains(@aria-label, 'Like')]")
    LIKE_COUNT = (By.XPATH, ".//a[contains(@href, '/liked_by/')]")
    BUTTON_NEXT_PHOTO = (By.XPATH, ".//button[contains(@aria-label, 'Next')]")
    BUTTON_PREVIOUS_PHOTO = (By.XPATH, ".//button[contains(@aria-label, 'Previous')]")

    def __init__(self, driver, root_element):
        super().__init__(driver)
        self.root_element = root_element

    # Методи для роботи з елементами
    def is_liked(self):
        return 'Unlike' in self.root_element.find_element(*self.LIKE_BUTTON).get_attribute('aria-label')

    def click_like(self):
        like_button = self.root_element.find_element(*self.LIKE_BUTTON)
        like_button.click()

    def get_like_count(self) -> int:
        try:
            count_text = self.root_element.find_element(*self.LIKE_COUNT).text
            return int(count_text.split()[0].replace(',', ''))
        except:
            return 0

    def click_next_photo(self) -> bool:
        next_button = self.root_element.find_element(*self.BUTTON_NEXT_PHOTO)
        next_button.click()
        return True

    def click_previous_photo(self) -> bool:
        prev_button = self.root_element.find_element(*self.BUTTON_PREVIOUS_PHOTO)
        prev_button.click()
        return True
