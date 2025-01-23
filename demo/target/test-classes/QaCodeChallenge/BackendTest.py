import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BackendTest(unittest.TestCase):

    def setUp(self):
        print("Setting up the WebDriver")
        edge_service = EdgeService(executable_path='C:/Users/Rahul/Selenium/demo/src/main/resources/Drivers/msedgedriver.exe')
        self.driver = webdriver.Edge(service=edge_service)
        self.driver.get("https://pns-p.dev.rfp.vmoamerica.com/api/docs/")
        self.wait = WebDriverWait(self.driver, 10)
        print("WebDriver setup complete")

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        print("Starting test_register_user")
        # POST
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'POST') and contains(text(), '/api/auth/register')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Try it out')]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//textarea"))).send_keys('''{
            "email": "test@example.com",
            "username": "testuser",
            "password": "password123"
        }''')
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Execute')]"))).click()

        # Print status code
        status_code = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Code')]/following-sibling::td"))).text
        print(f"Register User Status Code: {status_code}")

    def test_change_email(self):
        driver = self.driver
        wait = self.wait

        print("Starting test_change_email")
        # PATCH 
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'PATCH') and contains(text(), '/api/auth/change-email')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Try it out')]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//textarea"))).send_keys('''{
            "newEmail": "newemail@example.com",
            "password": "password123"
        }''')
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Execute')]"))).click()

        # Print status code
        status_code = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Code')]/following-sibling::td"))).text
        print(f"Change Email Status Code: {status_code}")

    def test_get_users(self):
        driver = self.driver
        wait = self.wait

        print("Starting test_get_users")
        # GET 
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'GET') and contains(text(), '/api/users')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Try it out')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Execute')]"))).click()

        # Print status code
        status_code = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Code')]/following-sibling::td"))).text
        print(f"Get Users Status Code: {status_code}")

    def tearDown(self):
        print("Tearing down the WebDriver")
        self.driver.quit()
        print("WebDriver teardown complete")

if __name__ == "__main__":
    unittest.main()