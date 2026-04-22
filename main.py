from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Running Selenium with a profile so we can bypass some login issues
profile_path = "/Users/ryanramdehol/Library/Application Support/Firefox/Profiles/vmjjns92.default-release"
options = Options()
options.profile = profile_path
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)
driver.get("https://www.google.com")
input("Press Enter to close...")
driver.quit()