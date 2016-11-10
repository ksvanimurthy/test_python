# from selenium_test.using_pytest.pytest_scripts.sign_in_out import *
# from selenium_test.using_pytest.pytest_scripts.buy_product import *
from selenium_test.using_pytest.pytest_scripts.sign_in_buy_sign_out import *


class Suite(unittest.TestCase):

    def suite(self):
        logging.info('Inside test suite')
        # self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(Test01SignInOut),
        #                                  unittest.defaultTestLoader.loadTestsFromTestCase(Test02BuyProduct),
        #                                  unittest.defaultTestLoader.loadTestsFromTestCase(Test03SignInBuySignOut)])
        self.suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(Test03SignInBuySignOut))
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
