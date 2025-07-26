
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME="Admin"
PASSWORD="admin123"

def login(driver):
    driver.get(URL)
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys("Admin")
    wait.until(EC.presence_of_element_located((By.NAME,"password"))).send_keys("admin123")
    wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
    print("Logged in Successfully ")