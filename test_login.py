from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import logging
import pytest

class Locators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='flash success']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='flash error']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("TestLogger")

logger = setup_logger()

@pytest.fixture(scope="function")
def setup_driver():
    logger.info("Setting up the WebDriver.")
    chrome_service = Service("D:/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    logger.info("Tearing down the WebDriver.")
    driver.quit()

def test_login_success(setup_driver):
    """Kiểm thử đăng nhập thành công"""
    logger.info("Testing successful login.")
    driver, wait = setup_driver
    try:
        driver.find_element(*Locators.USERNAME_INPUT).send_keys("tomsmith")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("SuperSecretPassword!")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        success_message = wait.until(
            EC.visibility_of_element_located(Locators.SUCCESS_MESSAGE)
        ).text

        logger.info("Success message received: %s", success_message)
        assert "You logged into a secure area!" in success_message
    except Exception as e:
        logger.error("Error during login success test: %s", e)
        raise

def test_login_failure(setup_driver):
    """Kiểm thử đăng nhập thất bại"""
    logger.info("Testing failed login.")
    driver, wait = setup_driver
    try:
        driver.find_element(*Locators.USERNAME_INPUT).send_keys("invalid_user")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("invalid_password")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        error_message = wait.until(
            EC.visibility_of_element_located(Locators.ERROR_MESSAGE)
        ).text

        logger.info("Error message received: %s", error_message)
        assert "Your username is invalid!" in error_message
    except Exception as e:
        logger.error("Error during login failure test: %s", e)
        raise

def test_logout(setup_driver):
    """Kiểm thử chức năng đăng xuất"""
    logger.info("Testing logout functionality.")
    driver, wait = setup_driver
    try:
        driver.find_element(*Locators.USERNAME_INPUT).send_keys("tomsmith")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("SuperSecretPassword!")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        logout_button = wait.until(
            EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        logout_message = wait.until(
            EC.visibility_of_element_located(Locators.SUCCESS_MESSAGE)
        ).text

        logger.info("Logout message received: %s", logout_message)
        assert "You logged out of the secure area!" in logout_message
    except Exception as e:
        logger.error("Error during logout test: %s", e)
        raise

# To generate an HTML report, run the tests using pytest-html:
# pytest --html=report.html
