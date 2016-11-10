from com.Shopclues.Library.baseLib import *

class FIlterProductTest(Intialization):

    def test_filtered_product_list(self):
        if not self.driver.find_element_by_name(self, 'Popular Categories').is_displayed() :
            self.driver._switch_to
