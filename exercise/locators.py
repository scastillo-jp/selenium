from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GET_NAME_SECTION = (By.XPATH, "//*[@id='grado']/div/div/div/div[1]/div/div")
    GET_LINKS = (By.CSS_SELECTOR, '.field-content>ul>li>a')
    GET_FACULTY = (By.XPATH, '//*[.="{}"]/ancestor::div[@class="panel panel-default"]//h4')
class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""

    pass