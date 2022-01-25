# Import Library
from selenium import webdriver
import pandas as pd
# Open Browser
driver = webdriver.Chrome()

# Get the  URL
url = 'https://www.geeksforgeeks.org/selenium-python-tutorial/'
driver.get(url)
driver.maximize_window()

# Read and Convert Web table into data frame
webtable_df = pd.read_html(driver.find_element_by_xpath("//*[@id='post-427949']/div[2]/table[1]").get_attribute('outerHTML'))[0]

# Write() to CSV file
webtable_df.to_csv('file2.csv')