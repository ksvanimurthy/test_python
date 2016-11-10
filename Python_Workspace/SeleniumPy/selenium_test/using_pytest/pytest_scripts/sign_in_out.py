from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium_test.using_pytest.pytest_library.base_lib import *
from selenium_test.using_pytest.pytest_pom.home_page import *


class Test01SignInOut(BaseLib, HomePage):

    def test_sign_in(self):
        self.driver.implicitly_wait(10)
        try:
            # self.driver.execute_script("window.alert('This is alert');")
            # time.sleep(5)
            # alert = self.driver.switch_to_alert()
            # alert.dismiss()
            # time.sleep(2)
            logging.info("Inside test_sign_in")
            self.driver.find_element(*HomePage.SIGNIN_LINK).click()
            logging.info("Clicked on Signin link")
            self.driver.find_element(*HomePage.EMAIL_TEXTBOX).send_keys(config.EMIAL_ID)
            logging.info('Login Email Id entered.')
            self.driver.find_element(*HomePage.PASSWORD_TEXTBOX).send_keys(config.EMAIL_PASSWORD)
            logging.info('Login Password entered.')
            self.driver.find_element(*HomePage.SIGNIN_BUTTON).click()
            logging.info('Clicked on Signin button for login Jabong.')
            error_msg_display = self.driver.find_element(*HomePage.ERROR_TEXT).is_displayed()
            if error_msg_display == True:
                logging.error('Oops....We have entered incorrect login Email Id or Password.')
            actualMsg = self.driver.find_element(*HomePage.ERROR_TEXT).text
            assert actualMsg == 'Incorrect username or password.'
            logging.info('Error message verified.')
            self.driver.find_element(*HomePage.SIGNIN_GOOGLE).click()
            logging.info('Trying to login via Google account.')
            self.driver.find_element(*HomePage.GMAIL_ID_TEXTBOX).send_keys(config.EMIAL_ID)
            self.driver.find_element(*HomePage.GMAIL_ID_NEXT_BUTTON).click()
            logging.info('Gmail login Id entered.')
            self.driver.find_element(*HomePage.GMAIL_PASSWORD_TEXTBOX).send_keys(config.EMAIL_PASSWORD)
            logging.info('Gmail login password entered.')
            self.driver.find_element(*HomePage.GMAIL_SIGNIN_BUTTON).click()
            logging.info('Clicked on Gmail Signin button.')
            account_loggedin = self.driver.find_element(*HomePage.ACCOUNT_LOGEDIN).is_displayed()
            if account_loggedin == True:
                logging.info('We have successfully logged in Jabong application.')
            logging.info("*****Congratulations we have successfully passed this Login to Jabong script.*****")

        except WebDriverException:
            logging.error('Exception raised in method - test_sign_in')
            self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_sign_in-"+BaseLib.now+".png")
            traceback.print_exc()
            logging.info("test_sign_in =" + "Fail")
            raise WebDriverException

# class TestBuyProduct(BaseLib, POM):
#
#     def test_buy_jersey(self):
#         self.driver.implicitly_wait(10)
#         try:
#             logging.info("Inside test_buy_jersey")
#             element = self.driver.find_element(*POM.SPORTS_SECTION)
#             ActionChains(self.driver).move_to_element(element).perform()
#             time.sleep(2)
#             logging.info("Clicked on Sports section")
#             self.driver.find_element(*POM.JERSEYS).click()
#             logging.info("Clicked on Jersey")
#             time.sleep(2)
#         except:
#             logging.error('Exception raised in method - test_buy_jersey')
#             self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_buy_jersey-"+BaseLib.now+".png")
#             traceback.print_exc()
#             logging.info("test_buy_jersey =" + "Fail")
#             raise WebDriverException
#
#     def test_buy_blazers(self):
#         self.driver.implicitly_wait(10)
#         try:
#             logging.info("Inside test_buy_blazers")
#             element = self.driver.find_element(*POM.MEN_SECTION)
#             ActionChains(self.driver).move_to_element(element).perform()
#             time.sleep(2)
#             logging.info("Clicked on Men section")
#             self.driver.find_element(*POM.SUITE_BLAZER).click()
#             logging.info("Clicked on Suits and blazers")
#             time.sleep(2)
#
#         except:
#             logging.error('Exception raised in method - test_buy_blazers')
#             self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_buy_blazers-"+BaseLib.now+".png")
#             traceback.print_exc()
#             logging.info("test_buy_blazers =" + "Fail")
#             raise WebDriverException