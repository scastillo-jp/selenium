
from element import BasePageElement
from locators import MainPageLocators
import pandas as pd

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    section = MainPageLocators.GET_NAME_SECTION

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Home page action methods come here"""

    # Declares a variable that will contain the retrieved text "grado"
    search_text_element = SearchTextElement()

    
    def is_title_matches(self):
        """Verifies that the hardcoded text "ESPOL - Educación" appears in page title"""

        return "ESPOL - Educación" in self.driver.title
    
    def create_csv_file(self):
        get_method = searchDataInGradoSection(self.driver)
        get_method.get_data_sections()


class searchDataInGradoSection(BasePage):
    "Search career_name_es, faculty_name, link_to_career_curriculum"

    def get_data_sections(self):
        career_names, faculty_name, career_links = [], [], []

        links = self.driver.find_elements(*MainPageLocators.GET_LINKS)
        
        for link in links:
            faculty = self.driver.find_element_by_xpath('//*[.="{}"]/ancestor::div[@class="panel panel-default"]//h4'.format(link.get_attribute('innerHTML')))
            career_names.append(link.get_attribute('innerHTML'))
            faculty_name.append(faculty.text)
            career_links.append(link.get_attribute('href'))
        
            # import methos exportDataToFileCsv to create file.csv
            export_data = exportDataToFileCsv(career_names, faculty_name, career_links)
            export_data.convert_to_csv()
        return "No results found." not in self.driver.page_source

class exportDataToFileCsv:
    """Export data received by parameters to CSV file"""

    career_names, faculty_name, career_links = [], [], []

    def __init__(self, career_names, faculty_name, career_links):  
        # defining constructor and parameters to use in the DataFrame
        self.career = career_names  
        self.faculty = faculty_name  
        self.links = career_links  

    def convert_to_csv(self):
        # retrive data from the parammeters career_names, faculty_name, career_links
        # and create the file CSV.
        df = pd.DataFrame({
            'career_name_es': self.career,
            'faculty_name' : self.faculty,
            'link_to_career_curriculum': self.links
            })

        df.to_csv('file.csv')