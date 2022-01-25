from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute('innerHTML')