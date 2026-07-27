from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    dashboard_heading = (By.XPATH,"//h6[text()='Dashboard']")
    
    def is_dashboard_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_heading))
    
    