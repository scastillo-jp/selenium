from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.espol.edu.ec/es/educacion")

assert "ESPOL - Educación" in driver.title

section = driver.find_element_by_xpath("//*[@id='grado']/div/div/div/div[1]/div/div")
innerFile = section.get_attribute('innerHTML')
career_names, faculty_name, career_links = [], [], []

if "Grado" in innerFile:
    links = driver.find_elements_by_css_selector('.field-content>ul>li>a')
    
    for link in links:
        faculty = driver.find_element_by_xpath('//*[.="{}"]/ancestor::div[@class="panel panel-default"]//h4'.format(link.get_attribute('innerHTML')))

        career_names.append(link.get_attribute('innerHTML'))
        faculty_name.append(faculty.text)
        career_links.append(link.get_attribute('href'))

    df = pd.DataFrame({
        'career_name_es': career_names,
        'faculty_name' : faculty_name,
        'link_to_career_curriculum': career_links
        })

    df.to_csv('file.csv')

else:
    print("Not found!")

assert "No results found." not in driver.page_source
driver.close()