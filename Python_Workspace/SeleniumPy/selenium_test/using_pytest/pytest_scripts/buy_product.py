from selenium_test.using_pytest.pytest_library.base_lib import *
from selenium_test.using_pytest.pytest_pom.home_page import *
from selenium_test.using_pytest.pytest_pom.men_section import *
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys


class Test02BuyProduct(BaseLib, HomePage, MenSection):

    # def test_buy_jersey(self):
    #     self.driver.implicitly_wait(10)
    #     try:
    #         logging.info("Inside test_buy_jersey")
    #         element = self.driver.find_element(*HomePage.SPORTS_SECTION)
    #         ActionChains(self.driver).move_to_element(element).perform()
    #         logging.info("Clicked on Sports section")
    #         time.sleep(2)
    #         self.driver.find_element(*HomePage.JERSEYS).is_displayed()
    #         time.sleep(2)
    #         self.driver.find_element(*HomePage.JERSEYS).click()
    #         logging.info("Clicked on Jersey")
    #         time.sleep(5)
    #         self.driver.execute_script("window.scrollTo(0,1000)")
    #         logging.info("Web page scrolled")
    #         time.sleep(5)
    #     except:
    #         logging.error('Exception raised in method - test_buy_jersey')
    #         self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_buy_jersey-"+BaseLib.now+".png")
    #         traceback.print_exc()
    #         logging.info("test_buy_jersey =" + "Fail")
    #         raise WebDriverException

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
            # if self.driver.find_element(*HomePage.SUITE_BLAZER).is_displayed():
            #     self.driver.find_element(*HomePage.SUITE_BLAZER).click()
            #     logging.info("Clicked on Suits and blazers")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0,1000)")
            # time.sleep(2)
            # self.click_filter_fit()
            # # self.driver.find_element(*MenSection.FILTER_FIT).click()
            # # logging.info("Clicked on Filter Fit")
            # time.sleep(2)
            # self.driver.find_element(*MenSection.FILTER_SLIM).click()
            # logging.info("Clicked on Slim Fit")
            # time.sleep(3)

        except:
            logging.error('Exception raised in method - test_buy_blazers')
            self.driver.save_screenshot(BaseLib.d + "\Reports\Screenshots\\test_buy_blazers-"+BaseLib.now+".png")
            traceback.print_exc()
            logging.info("test_buy_blazers =" + "Fail")
            raise WebDriverException
