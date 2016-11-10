from selenium.webdriver.common.by import By
from selenium_test.using_pytest.pytest_library.base_lib import *
from selenium.webdriver.common.action_chains import *


class MenSection:

    FILTER_FIT = (By.XPATH, "//ul[@id='filter-container']/li[@class='fit']")
    FILTER_SLIM = (By.XPATH, "//input[@type='checkbox' and @value='Slim']")
    SORT_FILTER = (By.XPATH, "//option[text()='Popularity']")
    IMAGE_CLICK = (By.XPATH, "//*[@id='catalog-product']/section[2]/div[2]/a/figure/img[@class= 'primary-image thumb loaded']")
    DATA_PRODUCT = (By.XPATH, "//*[@id='catalog-product']/section[2]/div[2]/a/figure/div[2]/div/p")
    DROP_DOWN = (By.XPATH, "//*[@id='size-drop-down']")
    ADD_TO_CART = (By.XPATH, "//*[@id='add-to-cart']")
    SELECT_SIZE = (By.XPATH, "//*[@id='size-block']/div[1]/ul/li[1]/a/span")
    CLICK_ON_BAG = (By.XPATH, "//*[@id='header-bag-sec']/a")
    PLACE_ORDER = (By.XPATH, "//*[@id='main']/div/section[2]/div[2]/div[2]/a")
    PRODUCT_IMAGE = (By.XPATH, "//*[@id='catalog-product']/section[2]/div[2]/a/figure/img")
    SEARCH_MENU = (By.XPATH, ".//*[@id='search']")


    def click_filter_fit(self):
        self.click_filter_fit().find_element(self.FILTER_FIT).click()
        logging.info("Clicked on Fit")
    #
    # def scroll_down(self):
    #     element = self.driver.find_element(self.FILTER_SLIM)
    #     ActionChains(self.driver).move_to_element(element).perform()
    #     logging.info('Scrolled down to Filter out products.')
    #     time.sleep(2)