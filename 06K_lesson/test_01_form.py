from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest
import time


@pytest.fixture
def driver():
    edge_options = EdgeOptions()
    edge_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()


def test_form_submission_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
    )
    
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    
    for field_name, value in fields.items():
        field = driver.find_element(By.NAME, field_name)
        field.clear()
        field.send_keys(value)
    
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    
    time.sleep(2)
    
    page_text = driver.find_element(By.TAG_NAME, "body").text
    print(f"\n=== ТЕКСТ СТРАНИЦЫ ===\n{page_text}\n======================\n")
    
    html = driver.page_source
    print(f"\n=== HTML СТРАНИЦЫ (первые 2000 символов) ===\n{html[:2000]}\n======================\n")
    