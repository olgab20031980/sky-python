from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    
    driver.get("https://httpbin.org/")
    
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()
    
    current_url = driver.current_url
    assert "/forms/post" in current_url, f"Expected URL to contain '/forms/post', but got {current_url}"
    
    driver.back()
    
    current_url = driver.current_url
    assert current_url == "https://httpbin.org/", f"Expected URL to be 'https://httpbin.org/', but got {current_url}"
    
    driver.quit()
