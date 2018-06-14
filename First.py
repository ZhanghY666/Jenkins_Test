import unittest,time
from selenium import webdriver

class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.testclass.net"

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_case(self):
        self.driver.get(self.base_url)
        secrch_input = self.driver.find_element_by_name("q")
        secrch_input.send_keys("jenkins")
        secrch_input.submit()

    def test_case2(self):
        self.driver.get(self.base_url)
        serch_input = self.driver.find_element_by_name("q")
        serch_input.send_keys("selenium")
        serch_input.submit()


if __name__ == '__main__':
    unittest.main()