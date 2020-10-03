import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
#     print("----init----")
#
#     if request.param == "chrome":
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#
#     if request.param == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = driver
#
#     yield
#     print("----close----")
#     driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title_test(self):
        self.driver.get("http://www.google.com")
        print(self.driver.title)
        assert self.driver.title == "Google"

    def test_google_URL_test(self):
        self.driver.get("http://www.google.com")
        print(self.driver.current_url)
        assert self.driver.current_url ==  "https://www.google.com/?gws_rd=ssl"
