from selenium.webdriver.common.by import By
import time

def test_check_add_to_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]'), 'Knopki nety'
    
