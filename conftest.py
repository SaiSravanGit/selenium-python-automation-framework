import pytest
import os
import re
from selenium import webdriver
from config.config import BASE_URL
from utils.DriverFactory import DriverFactory



@pytest.fixture
def driver():
    
    driver = DriverFactory.create_driver()
    
    driver.get(BASE_URL)
    
    yield driver
    
    driver.quit()
    
def pytest_runtest_makereport(item,call):
    
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver")
        
        if driver:
            os.makedirs("screenshots",exist_ok=True)
            
            # Identify the parallel worker running this test
            worker_id = getattr(
                item.config, "workerinput", {}
            ).get("workerid", "master")

            # Create a filesystem-safe, more unique filename
            safe_test_name = re.sub(
                r"[^A-Za-z0-9_.-]+", "_", item.nodeid
            )
            
            screenshot_name = f"{worker_id}_{safe_test_name}.png"
            screenshot_path = os.path.join(
                "screenshots", screenshot_name)
            
            driver.save_screenshot(screenshot_path)
            
        
        

    