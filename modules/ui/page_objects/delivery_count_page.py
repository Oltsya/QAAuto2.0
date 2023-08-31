from selenium import webdriver
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class DeliveryPage(BasePage):
    URL = "https://novaposhta.ua/delivery"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(DeliveryPage.URL)

    def close_add(self):
        close_btn = self.driver.find_element(
            By.XPATH, "//body/div[1]/div[3]/div[5]/div[1]/i"
        )
        close_btn.click()

    def select_city(self, city_element, city_name, id):
        # Click the element to open the suggestion list
        city_element.click()

        # Wait for the suggestion list is opened
        wait = WebDriverWait(self.driver, 10)
        suggestions_list = wait.until(EC.presence_of_element_located((By.ID, id)))

        # Find the proper city in the suggestion list
        found_city = False
        for index, city_option in enumerate(
            suggestions_list.find_elements(By.TAG_NAME, "li")
        ):
            if city_name in city_option.text:
                city_option.click()
                found_city = True
                break

        # Check if the proper city is found
        if not found_city:
            raise NoSuchElementException(
                f"City '{city_name}' is not in the suggestion list"
            )

        city_element.click()

    def count_delivery(
        self,
        city_from="Львів",
        city_to="Київ",
        newCargo_type="",
        newCount=1,
        newCost=457,
        newWeight=5,
        newLength=35,
        newWidth=45,
        newHeight=55,
        pack="f6f72e4b-5daf-11e3-b441-0050568002cf",
        floorCount=1,
        backDelivery=0,
    ):
        expected_price_range = "1,615.00 ... 1,915.00грн"
        sender_city = self.driver.find_element(By.ID, "DeliveryForm_senderCity")
        self.select_city(sender_city, city_from, "delivery_sender_cities")

        recipient_city = self.driver.find_element(By.ID, "DeliveryForm_recipientCity")
        self.select_city(recipient_city, city_to, "delivery_recipient_cities")

        cargo_type = self.driver.find_element(By.ID, "DeliveryForm_cargoType")
        self.driver.execute_script(
            "arguments[0].setAttribute('type', 'text')", cargo_type
        )
        cargo_type.send_keys(newCargo_type)

        count = self.driver.find_element(By.NAME, "DeliveryForm[optionsSeat][1][count]")
        count.send_keys(newCount)

        cost = self.driver.find_element(By.NAME, "DeliveryForm[optionsSeat][1][cost]")
        cost.send_keys(newCost)

        weight = self.driver.find_element(
            By.NAME, "DeliveryForm[optionsSeat][1][weight]"
        )
        weight.send_keys(newWeight)

        length = self.driver.find_element(
            By.NAME, "DeliveryForm[optionsSeat][1][volumetricLength]"
        )
        length.send_keys(newLength)

        width = self.driver.find_element(
            By.NAME, "DeliveryForm[optionsSeat][1][volumetricWidth]"
        )
        width.send_keys(newWidth)

        height = self.driver.find_element(
            By.NAME, "DeliveryForm[optionsSeat][1][volumetricHeight]"
        )
        height.send_keys(newHeight)

        packing = self.driver.find_element(By.ID, "add-pack")
        packing.send_keys(pack)

        floor_count = self.driver.find_element(By.ID, "DeliveryForm_floorCountAsc")
        floor_count.send_keys(floorCount)

        back_delivery = self.driver.find_element(By.ID, "DeliveryForm_backDelivery")
        back_delivery.send_keys(backDelivery)

        btn = self.driver.find_element(By.NAME, "yt0")
        """WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "yt0"))
        )"""

        btn.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "final")))
        total_price = self.driver.find_element(By.CLASS_NAME, "final").text

        assert (
            expected_price_range in total_price
        ), f"The total price is not exact as {expected_price_range}"

        # Повернення тексту з елементу "final" для подальшої перевірки, якщо необхідно
        return total_price

    def check_title(self, expected_title):
        return self.driver.title == expected_title
