from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()


login_url = "http://172.16.100.2:8090/httpclient.html"

roll_number = 'xyz'
try:
    driver.get(login_url)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button = driver.find_element(By.ID, "loginbutton")

    
    username_input.send_keys(roll_number)
    password_input.send_keys(roll_number)

    sign_in_button.click()

    status = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "signin-caption")))


    try:
        if "You are signed in as" in status.text:
                print(f"Login Success as {roll_number}")

        else:
                print("Login Failed.")

    except Exception as e:
            print(f"An error occurred: {e}")

except Exception as e:
    if 'Message: Element <input id="username" name="username" type="text"> is not reachable by keyboard' in str(e):
        print(" ")
    else:
        print(f"An error occurred: {e}")

finally:
    driver.quit()
