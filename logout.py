from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logout(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-userdropdown-name']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()
    print("Logged out")
