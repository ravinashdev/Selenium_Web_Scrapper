# ---------------------------- IMPORTS ------------------------------- #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
# Waiting classes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Time
from selenium.common.exceptions import TimeoutException
from datetime import datetime as dt, timedelta
import time
# Allows you to read the .env file
from dotenv import load_dotenv
import os
# ---------------------------- CONSTANTS ------------------------------- #
load_dotenv()
profile_path = os.environ.get("MOZILLA_PROFILE_PATH")
registration_email_text = os.getenv('GYM_PAGE_LOGIN_EMAIL')
registration_password_text = os.getenv('GYM_PAGE_LOGIN_PASSWORD')
now = dt.now()
six_days_later = now + timedelta(days=6)
formatted_six_days_later = six_days_later.strftime("%a, %b %d")
options = Options()
options.profile = profile_path
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)
# Initiate the wait class
wait = WebDriverWait(driver, 2)
driver.get("https://appbrewery.github.io/gym/")
# ---------------------------- FUNCTIONS ------------------------------- #
# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login_only():
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()
    login_form = wait.until(
        EC.presence_of_element_located((By.ID, "login-form"))
    )
    login_email = login_form.find_element(By.ID, "email-input")
    login_password = login_form.find_element(By.ID, "password-input")
    login_email.send_keys(f"{os.getenv('GYM_PAGE_LOGIN_EMAIL')}")
    login_password.send_keys(f"{os.getenv('GYM_PAGE_LOGIN_PASSWORD')}")
    login_form.find_element(By.ID, "submit-button").click()


def login_and_register(wait, driver):
    # Register a user for this instance since it's a localDB setup
    login_button = driver.find_element(By.ID, value="login-button")
    login_button.click()
    register_button = wait.until(
        EC.presence_of_element_located((By.ID, "toggle-login-register"))
    )
    register_button.click()
    registration_form = wait.until(
        EC.presence_of_element_located((By.ID, "login-form"))
    )
    registration_name = registration_form.find_element(By.ID, "name-input")
    registration_email = registration_form.find_element(By.ID, "email-input")
    registration_password = registration_form.find_element(By.ID, "password-input")
    registration_name.send_keys(f"Ryan Ramdehol")
    registration_email.send_keys(registration_email_text)
    registration_password.send_keys(registration_password_text)
    registration_form.find_element(By.ID, "submit-button").click()

def schedule_bookings():
    # Schedule a booking based on availability
    schedule_page = wait.until(
        EC.presence_of_element_located((By.ID, "schedule-page"))
    )
    bookings_grouped_by_day = schedule_page.find_elements(By.CSS_SELECTOR, value="[id^='day-group-']")
    # find a booking 1 week from today
    specific_booking_day_found = None
    # loop through all cards and find the day you're looking for
    for available_bookings_that_day in bookings_grouped_by_day:
        date = available_bookings_that_day.find_element(By.CSS_SELECTOR, value="[id^='day-title-']").text.strip()
        if date == formatted_six_days_later:
            specific_booking_day_found = available_bookings_that_day
    # loop through all available bookings that day and book all the classes that are not waitlisted
    available_bookings_that_day = specific_booking_day_found.find_elements(By.CSS_SELECTOR, value="[id^='class-card-']")
    for available_booking in available_bookings_that_day:
        get_state = available_booking.find_element(By.CSS_SELECTOR, value="[id^='book-button-']").text.strip()
        if get_state == "Book Class":
            available_booking.find_element(By.CSS_SELECTOR, value="[id^='book-button-']").click()

# ---------------------------- UI SETUP ------------------------------- #
# Running Selenium with a profile so we can bypass some login issues
retry(login_only, retries=7, description="Login Only")
retry(schedule_bookings, retries=7, description="Schedule Bookings")


















input("Press Enter to close...")
driver.quit()