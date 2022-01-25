from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.espol.edu.ec/es/educacion")
# assert "Grado" in driver.title
assert "ESPOL - Educación" in driver.title
section = driver.find_element_by_xpath("//*[@id='grado']/div/div/div/div[1]/div/div")
innerFile = section.get_attribute('innerHTML')
faculty_name = []
career_name_es = []

if "Grado" in innerFile:
    # find_section = driver.find_elements_by_xpath("//*[@id='views-bootstrap-accordion-1']")
    elems = driver.find_elements_by_css_selector('.panel-title>a')
    body = driver.find_elements_by_css_selector('.field-content>ul>li>a')
    links = driver.find_elements_by_css_selector('.field-content>ul>li [href]')

    links_path = [link.get_attribute('href') for link in links]
    links_name = [link.get_attribute('innerHTML') for link in links]


    for elem in elems:
        name_faculty = elem.get_attribute("innerHTML")
        faculty_name.append(name_faculty)


    # for bod in body:
    #     name = bod.get_attribute("innerHTML")
    #     career_name_es.append(name)

    df = pd.DataFrame({
        'career_name_es': links_name,
        'faculty_name' : 'faculty_name',
        'link_to_career_curriculum': links_path
        })
   
    df.to_csv('file.csv')



else:
    print("Not found!")
    
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()