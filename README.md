📘 README.md — OrangeHRM Automation Project
markdown
# 🧪 OrangeHRM Automation (Selenium + Python)

This project automates key workflows in the OrangeHRM demo application using Selenium WebDriver with Python. It replicates a real HR process from login to logout, including adding and searching for an employee.

---

## 🚀 Features Automated

- ✅ Login with valid credentials
- ✅ Add new employee (via PIM module)
- ✅ Search for newly added employee
- ✅ Logout from the session

---

## 🧰 Technologies Used

- Python
- Selenium WebDriver
- PyCharm IDE

---

## 🗂️ Project Structure

OrangeHRM_Automation/
├── driver_setup.py # Browser setup
├── login.py # Login functionality
├── add_employee.py # Add employee
├── search_employee.py # Search employee
├── logout.py # Logout
├── main.py # Run all tests
└── README.md # Project guide


---

## 🔧 Setup Instructions

1. ✅ Install Python  
2. ✅ Install Selenium:  
   ```bash
   pip install selenium
✅ Download ChromeDriver
Match your browser version from: https://chromedriver.chromium.org/downloads

Place chromedriver.exe inside your project or add it to system PATH

▶️ How to Run
Run the automation using:

  ```bash
  python main.py
Or, in PyCharm:

Right-click main.py → Run

🔐 Credentials Used
Username: Admin
Password: admin123

🎯 Why This Project?
This automation simulates a real-world HR workflow and demonstrates:

Clean modular coding using Page Object principles

Proper use of explicit waits for dynamic content

Scalable and maintainable structure for professional testing environments

📞 Author
Name: Kathiravan R
Designation : Q/A Engineer 
