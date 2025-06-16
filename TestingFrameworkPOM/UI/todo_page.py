from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TodoPage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://example.cypress.io/todo#/" 

    def go_to(self):
        self.driver.get(self.url)

    def add_todo(self, text):
        input_box = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-todo")))
        input_box.send_keys(text + "\n")

    def complete_todo(self, text):
        locator = (By.XPATH, f"//label[text()='{text}']/parent::div/input[@class='toggle']")
        checkbox = self.wait.until(EC.presence_of_element_located(locator))
        checkbox.click()

    def filter_by(self, filter_name):
        link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[text()='{filter_name}']"))
        )
        link.click()

    def todo_exists(self, text):
        locator = (By.XPATH, f"//label[text()='{text}']")
        return self.wait.until(EC.visibility_of_element_located(locator)) is not None

    def get_completed_todo_count(self):
        completed_items = self.driver.find_elements(
            By.XPATH, "//li[@class='completed']//input[@class='toggle' and @checked]"
        )
        return len(completed_items)