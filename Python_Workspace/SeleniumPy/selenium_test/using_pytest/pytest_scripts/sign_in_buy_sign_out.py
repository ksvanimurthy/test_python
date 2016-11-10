from selenium_test.using_pytest.pytest_library.base_lib import *
from selenium_test.using_pytest.pytest_pom.home_page import *
from selenium_test.using_pytest.pytest_pom.men_section import *
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys


class Test03SignInBuySignOut(BaseLib, HomePage, MenSection):

    def test_sign_in_buy_sign_out(self):
        self.driver.implicitly_wait(10)
        try:
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
            self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_sign_in-" + BaseLib.now + ".png")
            traceback.print_exc()
            logging.info("test_sign_in =" + "Fail")
            raise WebDriverException

    def test_buy_blazers(self):
        self.driver.implicitly_wait(10)
        try:
            logging.info("Inside test_buy_blazers")
            element = self.driver.find_element(*HomePage.MEN_SECTION)
            action = ActionChains(self.driver)
            action.move_to_element(element)
            action.context_click(element)
            action.key_down(Keys.SHIFT)
            action.send_keys('w')
            action.key_up(Keys.SHIFT).perform()
            time.sleep(15)
            logging.info("Men section opened in new Tab")
            ActionChains(self.driver).move_to_element(element).perform()
            logging.info("Clicked on Men section")
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "//div[@class='dropdown-container row']"
                                                             "//a[text()='Suits & Blazers']")))
            element.click()
            time.sleep(3)

            # element_1 = self.driver.find_element(*MenSection.IMAGE_CLICK)
            # assert element_1.click()
            # time.sleep(3)
            # element_2 = self.driver.find_element(*MenSection.DATA_PRODUCT)
            # assert element_2.click()
            self.driver.find_element(By.XPATH,"//*[@data-product-id='SU643MA12SRBINDFAS']").click()
            self.driver.find_element(By.XPATH, "//*[@id='size-block']/div[1]/ul/li[1]/a/span").click()
            self.driver.find_element(By.XPATH, "//*[@id='add-to-cart']").click()
            self.driver.find_element(By.XPATH, "//*[@id='header-bag-sec']/a").click()
            self.driver.find_element(By.XPATH, "//*[@id='main']/div/section[2]/div[2]/div[2]/a").click()

            # Add Address
            # self.driver.find_element(By.XPATH, ".//*[@id='postcode']").send_keys("560070")
            # self.driver.find_element(By.XPATH, ".//*[@id='first_name']").send_keys("Hello")
            # self.driver.find_element(By.XPATH, ".//*[@id='address1']").send_keys("123 street")
            # self.driver.find_element(By.XPATH, ".//*[@id='locality']").send_keys("JAYA")
            # self.driver.find_element(By.XPATH, ".//*[@id='phone']").send_keys("9900099887")
            # self.driver.find_element(By.XPATH, ".//*[@id='addressForm']/button").click()

        except:
            logging.error('Exception raised in method - test_buy_blazers')
            self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_buy_blazers-"+BaseLib.now+".png")
            traceback.print_exc()
            logging.info("test_buy_blazers =" + "Fail")
            raise WebDriverException