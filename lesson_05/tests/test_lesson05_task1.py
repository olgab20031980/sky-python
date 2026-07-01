from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://httpbin.org/")

    link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/forms/post']"))
    )
    link.click()

    wait.until(EC.url_contains("/forms/post"))
    current_url = driver.current_url
    assert "/forms/post" in current_url, (
        f"Expected URL to contain '/forms/post', but got {current_url}"
    )

    driver.back()

    wait.until(EC.url_contains("httpbin.org"))
    current_url = driver.current_url
    assert current_url == "https://httpbin.org/", (
        f"Expected URL to be 'https://httpbin.org/', but got {current_url}"
    )

    driver.quit()
