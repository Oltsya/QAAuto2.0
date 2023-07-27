import pytest


@pytest.mark.database
def test_create_table(database):
    table = database.create_table_discounts()

    # check that table is created
    assert len(table) == 0


@pytest.mark.database
def test_insert_discounts(database):
    database.insert_discounts(1, 1, 1, 350)
    value = database.get_discounts()

    # check the first record is created
    assert len(value) == 1

    # check the proper values in the table
    assert value[0][0] == 1
    assert value[0][1] == 1
    assert value[0][2] == 1
    assert value[0][3] == 350


@pytest.mark.database
def test_insert_discounts_wrong_types(database):
    with pytest.raises(TypeError):
        database.insert_discounts(1, "one", "two", 350)


@pytest.mark.database
def test_insert_discounts_extra_value(database):
    with pytest.raises(TypeError):
        database.insert_discounts(1, 1, 2, 350, 90)


@pytest.mark.database
def test_update_sum_in_discount_by_id(database):
    database.update_sum_in_discounts_by_id(1, 450)
    record = database.get_sum_in_discounts_by_id(1)

    # check that sum was changed for the first record
    assert record[0][0] == 450


@pytest.mark.database
def test_update_sum_in_discount_by_not_existing_id(database):
    with pytest.raises(ValueError):
        database.update_sum_in_discounts_by_id(999, 450)


@pytest.mark.database
def test_update_sum_in_discount_by_id_wrong_type(database):
    with pytest.raises(TypeError):
        database.update_sum_in_discounts_by_id(1, "450")


@pytest.mark.database
def test_get_all_records_by_foreign_keys(database):
    record = database.get_all_records_by_foreign_keys()

    # check the proper data in the table
    assert record[0][0] == 1
    assert record[0][1] == "Sergii"
    assert record[0][2] == "солодка вода"
    assert record[0][3] == 25
    assert record[0][4] == 450


@pytest.mark.database
def test_get_all_records_by_sum(database):
    database.insert_discounts(2, 2, 1, 500)
    database.insert_discounts(3, 1, 1, 350)
    record = database.get_all_records_by_sum(500)

    # check the proper data in the table
    assert record[0][0] == 2
    assert record[0][1] == "Stepan"
    assert record[0][2] == "солодка вода"
    assert record[0][3] == 25
    assert record[0][4] == 500


@pytest.mark.database
def test_get_all_records_by_wrong_sum(database):
    with pytest.raises(ValueError):
        database.get_all_records_by_sum(999)


@pytest.mark.database
def test_delete_record_by_id(database):
    database.delete_record_by_id(3)
    record = database.get_sum_in_discounts_by_id(3)

    # check the existence og the record
    assert len(record) == 0


@pytest.mark.database
def test_delete_all_records_from_discounts(database):
    database.delete_records_from_discounts()
    record = database.get_all_records_by_foreign_keys()

    # check the existence og the records
    assert len(record) == 0


@pytest.mark.database
def test_delete_table_discounts(database):
    database.drop_table_discounts()
