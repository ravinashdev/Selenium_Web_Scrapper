# ---------------------------- IMPORTS ------------------------------- #
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
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
driver.get("https://www.google.com")
input("Press Enter to close...")
driver.quit()