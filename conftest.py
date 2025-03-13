import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.customer_login_page import CustomerLoginPage
from pages.sale_page import SalePage


@pytest.fixture
def driver():
    # chrome_driver = webdriver.Chrome()
    # chrome_driver.maximize_window()
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver




@pytest.fixture()
def customer_login_page(driver):
    return CustomerLoginPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)