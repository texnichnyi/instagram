import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    BASE_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self._footer = None
        self.wait_for_loading()

    @property
    def footer(self):
        # Ініціалізувати футер, як тільки стане необхідно
        from page_objects.components.base_components.footer import Footer

        if self._footer is None:
            self._footer = Footer(self.driver)
        return self._footer

    # Очікування
    def wait_for_loading(self, element_locator: tuple = None):
        if element_locator:
            self.find_element(element_locator)

    def _wait_for_element(self, locator: tuple, condition: expected_conditions):
        try:
            element = WebDriverWait(self.driver, self.BASE_TIMEOUT).until(
                condition(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(
                f"{condition.__name__} не було виконано протягом {self.BASE_TIMEOUT} секунд. Локатор: {locator}"
            )

    # Методи для роботи з елементами
    def find_element(self, locator: tuple):
        return self._wait_for_element(locator, expected_conditions.presence_of_element_located)

    def find_elements(self, locator: tuple):
        self._wait_for_element(locator , expected_conditions.presence_of_all_elements_located)

    def click_element(self, locator: tuple):
        element = self._wait_for_element(locator, expected_conditions.element_to_be_clickable)
        element.click()

    def fill_text(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator: tuple, max_scrolls: int = 10, scroll_amount: int = 800) -> bool:
        scroll_count = 0
        while scroll_count < max_scrolls:
            elements = self.driver.find_element(locator)
            if elements:
                return True

            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            scroll_count += 1
            time.sleep(1)
        return False
