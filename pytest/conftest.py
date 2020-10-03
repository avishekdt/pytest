import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    print("----init----")

    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver

    yield
    print("----close----")
    driver.close()
