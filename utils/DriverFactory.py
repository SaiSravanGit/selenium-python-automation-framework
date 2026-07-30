from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import HEADLESS

class DriverFactory:
    
    
    @staticmethod
    def create_driver():
        
        options = Options()
        
        if HEADLESS:
            options.add_argument("--headless=new")
            options.add_argument("--windowsize=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        else:
            options.add_argument("--startmaximized")
            
        options.add_argument("--disable-notifications")
        
        
        
        return webdriver.Chrome(options=options)
    
