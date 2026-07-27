from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from testdata.login_data import LOGIN_TEST_DATA



@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected_result",LOGIN_TEST_DATA )


def test_login(driver,username,password,expected_result):
    
    
    login_page = LoginPage(driver)
    dashboard_page = login_page.login(username,password)
    
    if expected_result == 'valid':
        assert dashboard_page.is_dashboard_displayed()
    elif expected_result == 'invalid':
        assert login_page.is_login_error_displayed()
    

