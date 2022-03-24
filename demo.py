from time import sleep
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Look into Chrome Options

# Starts the session
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

# navigates to the link
driver.get("http://www.google.com")

# Request browser info
print(driver.title)

# Waiting startegies - Implicit, Others include fluent and explicit
driver.implicitly_wait(0.8)

# TEMP - REMOVE LATER
sleep(20)

# Finding Elements
search_box = driver.find_element(By.NAME,"q")
search_button = driver.find_element(By.NAME,"btnK")

# Taking Action on Element
search_box.send_keys("one piece")
search_button.click()

driver.implicitly_wait(30)




