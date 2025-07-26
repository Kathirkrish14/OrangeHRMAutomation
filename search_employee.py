from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_employee(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))).send_keys("John")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Search')]"))).click()
    print("🔍 Employee search completed")
