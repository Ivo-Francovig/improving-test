from selenium import webdriver
from UI.todo_page import TodoPage

def setup():
    driver = webdriver.Chrome()
    page = TodoPage(driver)
    page.go_to()
    return page, driver

def teardown(driver):
    driver.quit()

def test_add_complete_and_filter_todo():
    page, driver = setup()
    try:
        item = "Item nuevo"

        # Add item
        page.add_todo(item)
        assert page.todo_exists(item), "Todo was not added"

        # Wait for item to be present before completing
        print("Waiting for todo to be ready...")
        import time; time.sleep(1)  # Optional: small delay

        # Mark as completed
        page.complete_todo(item)

        # Filter by completed
        page.filter_by("Completed")

        # Verify only one item exists
        assert page.get_completed_todo_count() == 1, "Expected 1 completed todo"

        print("All assertions passed!")

    except Exception as e:
        print("Test failed:", str(e))
        driver.save_screenshot("error.png")
        raise

    finally:
        teardown(driver)

test_add_complete_and_filter_todo()