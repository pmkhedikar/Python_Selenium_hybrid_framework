from selenium.webdriver.common.by import By


class HomePage():
    # locators
    searchBox_xpath = "//*[@title='Search']"
    searchButton_xpath = "//*[@role='button' and @value='Search']"
    bookLink_xpath= "/(//ul[contains(@class, 'srp-results')]/li[contains(@class, 's-item')])[1]//a[contains(@class, 's-item__link')]/@href"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action steps
    def searchItem(self,searchKey):
        self.driver.find_element(By.XPATH, self.searchBox_xpath).send_keys(searchKey)

    def clickSearchbutton(self):
        self.driver.find_element(By.XPATH, self.searchButton_xpath).click()

    def clickOnBooklink(self):
        self.driver.find_element(By.XPATH, self.bookLink_xpath).click()

