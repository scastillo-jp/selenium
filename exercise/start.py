from selenium import webdriver
import page


driver = webdriver.Chrome()
driver.get("https://www.espol.edu.ec/es/educacion")

main_page = page.MainPage(driver)
main_page.verify_name_section()