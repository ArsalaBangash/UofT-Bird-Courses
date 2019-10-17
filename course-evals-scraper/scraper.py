# This scraper requires a valid UTOR login. You will be prompted for your UTORID and password
# when running this scraper because the website being scraped is behind an Acorn login screen

from getpass import getpass
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

quercus_url = "https://q.utoronto.ca/courses/48756/external_tools/291"
evals_url = "https://course-evals.utoronto.ca/BPI/fbview.aspx?blockid=hjeZ7JJWJupVgjPoyu&userid=tO4GQugFiFULB0AXgInh7idHCU-AnN3pNhvC&lng=en"

# Download the firefox gecko driver from https://github.com/mozilla/geckodriver/releases
driver = webdriver.Firefox()

driver.implicitly_wait(5)
driver.get(quercus_url)

# Elements from the acorn login page
utorid_input: WebElement = driver.find_element_by_id("username")
password_input: WebElement = driver.find_element_by_id("password")
login_button: WebElement = driver.find_element_by_name("_eventId_proceed")

# Prompts user for UTORID and password and logs into acorn with those details
# utorid = input("UTORID: ")
utorid_input.send_keys("utorid")
# password = getpass()
password_input.send_keys("password")
login_button.click()

# Once you're loggin in, navigate to the course evals URL
driver.get(evals_url)


# Elements from the course evals data page
hundred_button: WebElement = driver.find_element_by_css_selector("#fbvGridPageSizeSelectBlock > select:nth-child(1) > option:nth-child(7)")
grid: WebElement = driver.find_element_by_class_name("wsgridview")
rows = grid.find_elements_by_tag_name("tr")

# Fetch 100 evals at a time. 
time.sleep(2)
hundred_button.click()
rows = []
bird_courses = {} 

time.sleep(2)
for i in range(64):    ## Hardcoded. 
    next_button: WebElement = driver.find_element_by_css_selector(".gPaging > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(6) > input:nth-child(1)")
    table_rows = grid.find_elements_by_tag_name("tr")
    for table_row in range(1, len(table_rows)):
        rows.append(table_rows[table_row].text)
        item = table_rows[table_row].find_elements_by_tag_name("td")
        bird_courses[item[1].text] = item[6].text
    next_button.click()
    time.sleep(2)
print (bird_courses)

# This is the html we get from the page
html: property = driver.page_source
soup = BeautifulSoup(html, 'html')


# For now, all we do with the beautiful soup data model of our page is write it to an index.html
# file. #TODO: Parse this data and get the course eval info we're looking for
index = open("index.html", "w")
index.write(str(soup)) 