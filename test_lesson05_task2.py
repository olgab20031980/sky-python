from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    
    name_input = driver.find_element(By.NAME, "custname")
    
    name_input.send_keys("SkyPro Student")
    
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    
    current_url = driver.current_url
    assert "/post" in current_url, f"Expected URL to contain '/post', but got {current_url}"
    
    driver.quit()
