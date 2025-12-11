from selenium.webdriver.common.by import By
from page_objects.pages.base_page import BasePage


class BaseAuthPage(BasePage):
    """
    Сторінка BaseAuthPage, для всіх компонентів, які є базовими для залогованого користувача
    """
    MESSAGES_BUTTON = (By.XPATH, "(//*[local-name()='svg' and @aria-label='Messages'])[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._bottom_panel = None

    @property
    def bottom_panel(self):
        # Ініціалізувати нижню панель, як тільки стане необхідно
        from page_objects.components.base_components.bottom_panel import BottomPanel

        if self._bottom_panel is None:
            self._bottom_panel = BottomPanel(self.driver)
        return self._bottom_panel