from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class LoginPage(BasePage):
    
    username_textbox = (By.NAME,"username")
    password_textbox = (By.NAME,"password")
    login_button = (By.CLASS_NAME,"oxd-button")
    login_error_message = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    logger = get_logger(__name__)
    
    def __init__(self, driver):
        super().__init__(driver)
        
        
    def login(self,username,password):
        
        self.logger.info("Starting login process")        
        
        self.type(self.username_textbox,username)
        self.logger.info("Username entered")
        
        self.type(self.password_textbox,password)
        self.logger.info("Password entered")
        
        self.click(self.login_button)
        self.logger.info("Login button clicked")
        
        return DashboardPage(self.driver)
    
    def is_login_error_displayed(self):
        
        return self.wait.until(EC.visibility_of_element_located(self.login_error_message)).is_displayed()
    
    


        
