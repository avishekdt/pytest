import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    print("----init----")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("----close----")
    driver.quit()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    print("----init ff----")

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("----close----")
    driver.quit()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass


class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


# ff
@pytest.mark.usefixtures("init_ff_driver")
class Base_FF_Test:
    pass


class Test_Google_FF(Base_FF_Test):
    def test_google_title_ff(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
