from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RozetkaMainPage(BasePage):
    URL = "https://rozetka.com.ua/ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaMainPage.URL)

    """def open_sergii_prytula_page(self):
        menu_btn = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/rz-mobile-user-menu/button",
        )
        menu_btn.click()

        wait = WebDriverWait(self.driver, 10)
        result_element = wait.until(EC.presence_of_element_located((By.ID, "fat-menu")))
        wait.until(EC.element_to_be_clickable((By.ID, "fat-menu")))

        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click the link which opens a new window
        prytula_btn = self.driver.find_element(
            By.XPATH,
            "//*[@id='cdk-overlay-0']/nav/div/div[2]/rz-charitable-foundation/a",
        )
        prytula_btn.is_selected()

        # Wait for the new window or tab
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Check the proper title of the new window
        return self.driver.title == "LiqPay БО Благодійний Фонд Сергія Притули"

        wait = WebDriverWait(self.driver, 10)
        result_element = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/rz-header-fat-menu/rz-fat-menu/div[2]/ul/li[1]/a",
                )
            )
        )"""

    def pick_category(self, category_xpath):
        current_title = self.driver.title

        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click the link which opens a new window
        category_elem = self.driver.find_element(By.XPATH, category_xpath)
        category_elem.click()

        # Wait for the new window or tab
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Check the proper title of the new window
        try:
            # Wait for the new page to load (title changes)
            wait.until(EC.title_is_not(current_title))
        except TimeoutException:
            raise AssertionError("The title is not changed")

    def filter_by_brand(self, brand_xpath):
        brand_elem = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-producer/div/section/div/app-slider/div/div/rz-combine-scrollbar/div/div[1]/div/ul/li[1]/a/img",
        )
        brand_elem.is_selected()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
