import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.espol.edu.ec/es/educacion")

    def test_search_in_espol_site(self):
        """Searches for the title "ESPOL - Educación" then
        verified that some results show up"""

        #Load the main page. In this case the home page of www.espol.edu.ec/es/educacion
        main_page = page.MainPage(self.driver)
        #Checks if the word "ESPOL - Educación" is in title
        assert main_page.is_title_matches(), "ESPOL - Educación title doesn't match."
        
    def test_set_section_to_find(self):
        """"Set name section to find or search in the page"""

        # Sets the text of grado"
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "grado"
        assert main_page.search_text_element, "grado section doesn't match."


    def test_verify_that_the_results_page_is_not_empty(self):
        """"Verifies that the results method searchDataInGradoSection is not empty"""
        search_results_page = page.searchDataInGradoSection(self.driver)

        #Verifies that the results page is not empty
        assert search_results_page.get_data_sections(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()