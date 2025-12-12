from page_objects.pages.base_page import BasePage


class BaseUnathorizedPage(BasePage):
    """
    Сторінка BaseUnathorizedPage, для всіх компонентів, які є базовими для не залогованого користувача
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._footer = None

    @property
    def footer(self):
        # Ініціалізувати футер, як тільки стане необхідно
        from page_objects.components.base_components.footer import Footer

        if self._footer is None:
            self._footer = Footer(self.driver)
        return self._footer
