import unittest
from appium import webdriver

class BaseLib(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

    def setUp(self):
        desired_capabilities = {}
        desired_capabilities['platformName'] = 'Android'
        desired_capabilities['platformVersion'] = '4.4.4'
        desired_capabilities['deviceName'] = 'redmi2'
        desired_capabilities['appPackage'] = 'com.shopclues'
        desired_capabilities['appActivity'] = '.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader.loadTestsFromTestCase(BaseLib)
    unittest.TextTestRunner(verbosity=1).run(suite)