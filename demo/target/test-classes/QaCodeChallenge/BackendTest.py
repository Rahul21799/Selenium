from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://pns-p.dev.rfp.vmoamerica.com/api/docs/")
    self.wait = WebDriverWait(self.driver, 10)

def test_register_user(self):
    driver = self.driver
    wait = self.wait

    # POST
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'POST') and contains(text(), '/api/auth/register')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Try it out')]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea"))).send_keys('''{
        "email": "test@example.com",
        "username": "testuser",
        "password": "password123"
    }''')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Execute')]"))).click()

   
def test_change_email(self):
    driver = self.driver
    wait = self.wait

    # PATCH 
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'PATCH') and contains(text(), '/api/auth/change-email')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Try it out')]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea"))).send_keys('''{
        "newEmail": "newemail@example.com",
        "password": "password123"
    }''')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Execute')]"))).click()

   

def test_get_users(self):
    driver = self.driver
    wait = self.wait

    # GET 
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'GET') and contains(text(), '/api/users')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Try it out')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Execute')]"))).click()

    

def tearDown(self):
    self.driver.quit()