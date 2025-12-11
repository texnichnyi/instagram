from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.safari.options import Options as SafariOptions


class DriverManager:
    LOAD_PAGE_TIMEOUT = 2

    def __init__(self, browser_name: str):
        self.browser_name = browser_name

    def __get_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(self.LOAD_PAGE_TIMEOUT)

        return driver

    def __get_safari_driver(self):
        options = SafariOptions()
        driver = webdriver.Safari(options=options)
        driver.maximize_window()
        driver.implicitly_wait(self.LOAD_PAGE_TIMEOUT)

        return driver

    def get_driver(self):
        if self.browser_name == 'chrome':
            return self.__get_chrome_driver()
        elif self.browser_name == 'safari':
            return self.__get_safari_driver()
        else:
            raise ValueError("Добавте реалізацію бажаного драйвера.")

    @staticmethod
    def quit_driver(driver):
        if driver:
            driver.quit()
