from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        def get_cookies(username, password):
            driver.get("https://gitflic.ru/")
            driver.find_element(By.CSS_SELECTOR, "a[href*='login']").click()
            driver.find_element(
                By.CSS_SELECTOR, "input[type='email']"
                ).send_keys(username)
            driver.find_element(
                By.CSS_SELECTOR, "input[type='password']"
                ).send_keys(password)
            driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']"
                ).click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, ".user-profile"))
                )
            return driver.get_cookies()

        user1_cookies = get_cookies("user1@email.com", "password1")
        user2_cookies = get_cookies("user2@email.com", "password2")

        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/")
        for c in user1_cookies:
            driver.add_cookie({'name': c['name'], 'value': c['value']})
        driver.refresh()
        driver.get("https://gitflic.ru/user/username1")
        url1 = driver.current_url

        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/")
        for c in user2_cookies:
            driver.add_cookie({'name': c['name'], 'value': c['value']})
        driver.refresh()
        driver.get("https://gitflic.ru/user/username2")
        url2 = driver.current_url

        assert url1 != url2, "URLs are the same"
        print("Test passed")

    finally:
        driver.quit()
