import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(r"C:/Users/vovaf/starting_git/QAAuto2.0" + "chromedriver.exe")
    )
    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, "login_field")

    login_elem.send_keys("onetwothree@gmail.com")

    pass_elem = driver.find_element(By.ID, "password")

    pass_elem.send_keys("one1234")

    btn = driver.find_element(By.NAME, "commit")

    btn.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
