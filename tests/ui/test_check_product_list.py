import pytest
from modules.ui.page_objects.main_page_rozetka import RozetkaMainPage


@pytest.mark.uirozetka
def test_pick_category():
    main_page = RozetkaMainPage()

    main_page.go_to()

    main_page.pick_category(
        "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[1]/rz-sidebar-fat-menu/div/ul/li[1]/a"
    )

    main_page.check_title(
        "Комп'ютери та ноутбуки - ROZETKA | Комп'ютери та ноутбуки у Києві, Харкові, Одесі, Львові: ціна, відгуки, продаж оптом комп'ютерів і ноутбуків"
    )


@pytest.mark.uirozetka
def test_filter_by_brand():
    main_page = RozetkaMainPage()

    main_page.go_to()

    main_page.pick_category(
        "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[1]/rz-sidebar-fat-menu/div/ul/li[1]/a"
    )

    main_page.filter_by_brand(
        "/html/body/app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-producer/div/section/div/app-slider/div/div/rz-combine-scrollbar/div/div[1]/div/ul/li[1]/a"
    )

    main_page.check_title(
        "Купити гаджети та аксесуари Apple у Киеві: ціна, відгуки, продаж"
    )


"""@pytest.mark.uirozetka
def test_prytula_page_open():
    main_page = RozetkaMainPage()

    main_page.open_sergii_prytula_page()"""
