import os.path
import time

import pytest
from webdriver_manager.core import driver

from pageObjects.HomePage import HomePage
from pageObjects.ItemPage import ItemPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_SearchItem():
    baseURL = ReadConfig.getAppUrl()
    logger= LogGen.loggen()
    search_key ="book"

    @pytest.mark.sanity
    def test_search_item(self,setup):
        self.logger.info("********* Test_001_SearchItem Started ********")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # created the object of class
        self.hp.searchItem(self.search_key)
        self.hp.clickSearchbutton(self.driver)
        self.hp.clickOnBooklink()(self.driver)
        time.sleep(5)

        self.ip = ItemPage(self.driver)
        self.ip.clickAddToCart(self.driver)


        try:
            cart_value = self.ip.getCartValue(self.driver)
            if int(cart_value) > 0:
                print("Test Passed: item added successfully to cart")
            else:
                print("Test Failed: Cart value not updated")
        except:
            print("Test Failed: Cart badge not found.")

        finally:
            # Close the browser
            self.logger.info("********* Test Test_001_SearchItem finished ***********")
            driver.quit()






