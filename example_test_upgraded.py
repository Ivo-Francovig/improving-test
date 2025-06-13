from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://example.cypress.io/todo#/" 
TIMEOUT = 15

driver = webdriver.Chrome()
wait = WebDriverWait(driver, TIMEOUT)

try:
    # Go to url
    driver.maximize_window()
    driver.get(URL)

    # Add new to do item
    new_item = "Item nuevo"
    new_todo_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-todo")))
    new_todo_input.send_keys(new_item + Keys.ENTER)
    print("New Item Created")

    # Mark as completed
    checkbox = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//label[text()='{new_item}']/preceding-sibling::input"))
    )
    checkbox.click()
    assert checkbox.is_selected(), "Checkbox was not selected"
    print("New Item Selected")

    # Filter by completed
    completed_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Completed"))
    )
    completed_link.click()
    print("Filter Changed to Completed")

    # Wait for filtered results
    wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//label[text()='{new_item}']"))
    )
    print("Successfully filtered to completed items")

except Exception as e:
    print(f"Execution failed: {e}")
    driver.save_screenshot("test_failure.png")
    raise

finally:
    driver.quit()