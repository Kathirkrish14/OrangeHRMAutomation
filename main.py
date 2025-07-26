from driver_setup import setup_driver
from login import login
from add_employee import add_employee
from search_employee import search_employee
from logout import logout

driver = setup_driver()

try:
    login(driver)
    add_employee(driver)
    search_employee(driver)
    logout(driver)
    print("\n All actions completed successfully!")
except Exception as e:
    print("Something went wrong:", e)
finally:
    driver.quit()
