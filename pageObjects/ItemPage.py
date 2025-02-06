from selenium.webdriver.common.by import By

class ItemPage():
    addToCart_xpath = "//span[text()[contains(.,'Add to cart')]]"
    cartValue_xpath= "//*[@class='badge']"

    def __init__(self,driver):
        self.driver= driver

    def clickAddToCart(self):
        self.driver.find_element(By.XPATH,self.addToCart_xpath).click()

    def getCartValue(self):
        self.driver.find_element(By.XPATH, self.cartValue_xpath).text

