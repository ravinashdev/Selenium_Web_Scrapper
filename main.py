# ---------------------------- IMPORTS ------------------------------- #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
# Waiting classes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Allows you to read the .env file
from dotenv import load_dotenv
import os
# ---------------------------- CONSTANTS ------------------------------- #
load_dotenv()

# ---------------------------- UI SETUP ------------------------------- #
# Running Selenium with a profile so we can bypass some login issues
profile_path = os.environ.get("MOZILLA_PROFILE_PATH")
options = Options()
options.profile = profile_path
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)
# Initiate the wait class
wait = WebDriverWait(driver, 10)

driver.get("https://appbrewery.github.io/gym/")
# Register a user for this instance since it's a localDB setup
login_button = driver.find_element(By.ID, value="login-button")
login_button.click()
register_button = driver.find_element(By.ID, value="toggle-login-register").click()
registration_form = wait.until(
    EC.presence_of_element_located((By.ID, "login-form"))
)
registration_name = registration_form.find_element(By.ID, "name-input")
registration_email = registration_form.find_element(By.ID, "email-input")
registration_password = registration_form.find_element(By.ID, "password-input")

registration_name.send_keys(f"Ryan Ramdehol")
registration_email.send_keys(f"{os.getenv('GYM_PAGE_LOGIN_EMAIL')}")
registration_password.send_keys(f"{os.getenv('GYM_PAGE_LOGIN_PASSWORD')}")

registration_form.find_element(By.ID, "submit-button").click()

# Login User
# login_button = driver.find_element(By.ID, value="login-button")
# login_button.click()
# login_form = wait.until(
#     EC.presence_of_element_located((By.ID, "login-form"))
# )
# login_email = login_form.find_element(By.ID, "email-input")
# login_password = login_form.find_element(By.ID, "password-input")
# login_email.send_keys(f"{os.getenv('GYM_PAGE_LOGIN_EMAIL')}")
# login_password.send_keys(f"{os.getenv('GYM_PAGE_LOGIN_PASSWORD')}")


input("Press Enter to close...")
driver.quit()