from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://httpbin.org/forms/post")

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("SkyPro Student")

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    wait.until(EC.url_contains("/post"))
    current_url = driver.current_url
    assert "/post" in current_url, (
        f"Expected URL to contain '/post', but got {current_url}"
    )

    driver.quit()
