from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
def test_verify_home_page(driver):
    pass

def test_verify_manage_booking_widget(driver):
    driver.find_element_by_css_selector('div.widgetBoxWrapper > ul li:nth-of-type(2)').click()
 
def test_verify_checkin_widget(driver):
    driver.find_element_by_css_selector('div.widgetBoxWrapper > ul li:nth-of-type(3)').click()
 
def test_verify_flight_status_widget(driver):
    driver.find_element_by_css_selector('div.widgetBoxWrapper > ul li:nth-of-type(4)').click()
    
def test_verify_search_ow_results_page(driver):
    driver.find_element_by_css_selector('div.widgetBoxWrapper .radio-oneway-div').click()
    driver.find_element_by_css_selector('div.widgetBoxWrapper #airport-destination').click()
    driver.find_element_by_css_selector('.DestinationAirlist li[data-value=\'MCT\']').click()
    driver.execute_script('date = new Date();date.setDate(date.getDate()+20);document.getElementById("FormModel_DepartureDate").value=""+date')
    driver.find_element_by_css_selector("div.widgetBoxWrapper input[value='Search']").click()
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.tripSummaryBox')))
