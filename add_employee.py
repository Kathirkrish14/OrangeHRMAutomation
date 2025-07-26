from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_employee(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("John")
    wait.until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("Doe")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    print("Employee added")
