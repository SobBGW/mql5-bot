from concurrent.futures import thread
from time import sleep
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Look into Chrome Options

# Starts the session
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

# Delay
driver.implicitly_wait(1)

# Navigate to login page
driver.get("https://www.mql5.com/en/auth_login")


# Delay - ensure page is fully loaded
driver.implicitly_wait(2)

# Locate the login Form (Email & Password Fields)
email_field = driver.find_element(By.NAME, "Login")
password_field = driver.find_element(By.NAME, "Password")
login_button = driver.find_element(By.CLASS_NAME,"qa-submit")

# Delay
driver.implicitly_wait(5)

# Send login Details to Email and Password Fields
email_field.send_keys("yolo11")
password_field.send_keys("bp7xHaJR")

# Delay wait before logging in
driver.implicitly_wait(10)

login_button.click()

# Delay - let the page load up
driver.implicitly_wait(1000)

# Open a new tab
driver.switch_to.new_window('tab')

# Delay wait before accessing profiles

# TEST - REMOVE LATER
links = ['https://www.mql5.com/en/users/sendend', 'https://www.mql5.com/en/users/amorthem']
salutation = "Hello, "
message = "I have been analysing your trading systems and i'm really impressed. \n \n If this is something of interest to you I would like to express a partnership proposal. \n \n Kind Regards, \n \n Sean"

for i in range(len(links)):
    # Get first profile link
    driver.get(str(links[i]))

    # Delay let the page fully load
    driver.implicitly_wait(10)

    # Locate and Press the profile button
    profile_button = driver.find_element(By.CLASS_NAME, "tree-menu__link")
    profile_button.click()

    # Delay let the page fully load
    driver.implicitly_wait(10)

    # Locate and Press the add friend button
    try:
        add_friend_button = driver.find_element(By.CLASS_NAME, "qa-add-to-friends")
        add_friend_button.click()
    except:
        print("Was not able to add this user as a friend, This account may already be a friend")

    # Delay wait for page to load up
    driver.implicitly_wait(10)

    # Locate the Profile Username
    user_name = driver.find_element(By.CLASS_NAME, "user-page__name").text

    # Locate and Press the send message button
    send_message_button = driver.find_element(By.CLASS_NAME, "qa-send-message")
    send_message_button.click()

    # Delay wait for the message prompt to load
    driver.implicitly_wait(10)

    # Locate the text field and Send button
    text_area = driver.find_element(By.CLASS_NAME, "chat-editor__textarea")
    send_button = driver.find_element(By.CLASS_NAME, "button_widget")
    
    # Message construction
    final_message = str(salutation) + str(user_name) + str("\n \n") + str(message)

    # Send Message to textarea
    text_area.send_keys(final_message)

    # Delay before pressing the send button
    driver.implicitly_wait(10)
    # Press Send button
    # send_button.click()


    sleep(10)


sleep(50)
