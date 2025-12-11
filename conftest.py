import pytest

from driver.driver_manager import DriverManager
from page_objects.pages.login_page.login_page import LoginPage
from page_objects.pages.sign_up_page.sing_up_page import SignUpPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chrome",
        help="Specify browser name"
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser-name")


@pytest.fixture(scope="function")
def driver(browser_name):
    setup = DriverManager(browser_name=browser_name)
    web_driver = setup.get_driver()
    yield web_driver
    setup.quit_driver(web_driver)


@pytest.fixture(scope="function")
def login_page(driver):
    base_url = "https://www.instagram.com/"
    driver.get(base_url)
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture(scope="function")
def sign_up_page(driver):
    sign_up_url = "https://www.instagram.com/accounts/emailsignup/"
    driver.get(sign_up_url)
    sign_up_page = SignUpPage(driver)
    return sign_up_page
