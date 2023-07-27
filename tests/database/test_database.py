import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    # Print the result in the terminal
    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    record = database.get_user_address_by_name("Sergii")

    # Check the structure of result
    assert record[0][0] == "Maydan Nezalezhnosti 1"
    assert record[0][1] == "Kyiv"
    assert record[0][2] == "3127"
    assert record[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    record = database.select_product_qnt_by_id(1)

    # Check that quantity changed to 25 in order 1
    assert record[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, "печиво", "солодке", 30)
    record = database.select_product_qnt_by_id(4)

    # Check that quantity equals 30 in order 4
    assert record[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, "чіпси", "снеки", 999)
    database.delete_product_by_id(99)
    record = database.select_product_qnt_by_id(99)

    # Check that there is no results on select request
    assert len(record) == 0


@pytest.mark.database
def test_detailed_orders(database):
    record = database.get_detailed_orders()
    # print the result in terminal
    print(record)

    # Check that there is only one result
    assert len(record) == 1

    # Check the structure of the result
    assert record[0][0] == 1
    assert record[0][1] == "Sergii"
    assert record[0][2] == "солодка вода"
    assert record[0][3] == "з цукром"
