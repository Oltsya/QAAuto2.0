from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class SignInRozetka(BasePage):
    URL = "https://rozetka.com.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInRozetka.URL)

    def try_login_modal(self):
        login_btn = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button",
        )
        login_btn.click()

        """wait = WebDriverWait(self.driver, 10)
        result_element = wait.until(
            EC.presence_of_element_located((By.ID, "auth_email"))
        )"""

    def try_login(self, login, password):
        login_elem = self.driver.find_element(By.ID, "auth_email")
        login_elem.send_keys(login)

        try:
            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[1]/p",
                    )
                )
            )
            if error_message_element.is_displayed():
                raise AssertionError("The login is not valid")
        except TimeoutException:
            pass

        pass_elem = self.driver.find_element(By.ID, "auth_pass")
        pass_elem.send_keys(password)

        sign_in_btn = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]",
        )
        sign_in_btn.click()

        try:
            error_message_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        # this is xpath of the error message
                        # "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[2]/div[2]",
                        # due to the problem with CAPTCHA I've changed xpath to the CAPTCHA's one
                        "//*[@id='ngrecaptcha-0']",
                    )
                )
            )
            if error_message_element.is_displayed():
                raise AssertionError("The CAPTCHA is on, can't continue")
        except TimeoutException:
            pass

    def forgot_password(self, login):
        login_elem = self.driver.find_element(By.ID, "auth_email")
        login_elem.send_keys(login)

        forgot_pass_elem = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[3]/a",
        )
        forgot_pass_elem.click()

        confirmation_button_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[3]/button",
                )
            )
        )

    def sign_in_with_other_app(self, xpath, expected_window_title):
        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click the link which opens in a new window
        new_app__button_elem = self.driver.find_element(By.XPATH, xpath)
        new_app__button_elem.click()

        # Wait for the new window or tab
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Check the proper window is opened
        return self.driver.title == expected_window_title

    def sign_in_as_new_user(self):
        register_buton = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[2]",
        )
        register_buton.click()

        wait = WebDriverWait(self.driver, 10)
        result_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/rz-single-modal-window/div[3]/div[1]")
            )
        )

    def check_title(self, expected_title):
        return self.driver.title == expected_title
