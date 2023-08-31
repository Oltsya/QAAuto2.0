import pytest
from modules.ui.page_objects.delivery_count_page import DeliveryPage
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.uidelivery
def test_delivery_count_proper_values(ui_delivery):
    ui_delivery.count_delivery()

    ui_delivery.check_title("Вартість доставки - «Нова Пошта»| Доставка майбутнього")


@pytest.mark.uidelivery
def test_delivery_count_invalid_total_price(ui_delivery):
    try:
        ui_delivery.count_delivery(
            city_from="Вінниця",
            city_to="Дніпро",
            newCost=700,
            newWeight=10,
            newLength=15,
            newWidth=15,
            newHeight=60,
        )

    except AssertionError as e:
        assert "The total price is not exact as {expected_price_range}"
    else:
        pytest.fail("Test didn't rise AssertionError for the wrong total price")

    ui_delivery.check_title("Вартість доставки - «Нова Пошта»| Доставка майбутнього")


@pytest.mark.uidelivery
def test_delivery_count_invalid_sender_city(ui_delivery):
    try:
        ui_delivery.count_delivery(city_from="Ккккиїв")

    except NoSuchElementException as e:
        assert f"This city is not in the suggestion list"
    else:
        assert False, "Test didn't rise NoSuchElementException for not existing city"

    ui_delivery.check_title("Вартість доставки - «Нова Пошта»| Доставка майбутнього")
