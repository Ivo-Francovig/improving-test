#Agregar 1 item
#Seleccionar ese item
#Filtrar Completed

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.maximize_window()

driver.get("https://example.cypress.io/todo#/")

try:
    input_new_item = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-todo")))

    new_item = "Item nuevo"
    input_new_item.send_keys(new_item)
    input_new_item.send_keys(Keys.ENTER)
    print("New Item Created")

    checkbox_new_item = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Item nuevo')]//parent::div/input")))

    checkbox_new_item.click()

    assert checkbox_new_item.is_selected()

    print("New Item Selected")

    btn_completed = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#/completed']")))

    btn_completed.click()

    assert btn_completed.is_selected()

    print("Button pressed")

except:
    print("Execution failed")
    driver.save_screenshot("test_fail.png")

finally: 
    driver.quit()



