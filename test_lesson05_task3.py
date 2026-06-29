from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    
    all_links = driver.find_elements(By.TAG_NAME, "a")
    
    expected_count = 9
    actual_count = len(all_links)
    assert actual_count == expected_count, f"Expected {expected_count} links, but found {actual_count}"
    
    for i, link in enumerate(all_links):
        assert link.is_displayed(), f"Link at index {i} is not displayed"
    
    first_link_text = all_links[0].text
    assert "1" in first_link_text, f"Expected first link text to contain '1', but got '{first_link_text}'"
    
    driver.quit()
    