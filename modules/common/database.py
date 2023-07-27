import _sqlite3


class Database:
    def __init__(self):
        self.connection = _sqlite3.connect(
            "C:/Users/vovaf/starting_git/QAAuto2.0" + "/become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()

        print(f"Connected successfully. SQLite Database version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity)\
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date FROM orders\
            JOIN customers ON orders.customer_id = customers.id\
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    # For individual QAAuto task
    def create_table_discounts(self):
        query = "CREATE TABLE discounts (\
            id int NOT NULL,\
            customer_id int,\
            order_id int,\
            sum int,\
            PRIMARY KEY (id),\
            FOREIGN KEY (customer_id) REFERENCES customers(id),\
            FOREIGN KEY (order_id) REFERENCES orders(id))"
        self.cursor.execute(query)
        self.connection.commit()
        table = self.cursor.fetchall()

        return table

    def insert_discounts(self, id, customer_id, order_id, sum):
        if not all(isinstance(val, int) for val in (id, customer_id, order_id, sum)):
            raise TypeError("Wrong data type!")

        query = f"INSERT INTO discounts (id, customer_id, order_id, sum)\
            VALUES ({id}, {customer_id}, {order_id}, {sum})"
        value = self.cursor.execute(query)
        self.connection.commit()

        return value

    def get_discounts(self):
        query = "SELECT * FROM discounts"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_sum_in_discounts_by_id(self, id, new_sum):
        if not all(isinstance(val, int) for val in (id, new_sum)):
            raise TypeError("Wrong data type!")
        records = self.get_discounts()
        found_id = False

        for record in records:
            if record[0] == id:
                found_id = True
                break

        if not found_id:
            raise ValueError(
                f"Discount with id {id} does not exist in the discounts table!"
            )

        query = f"UPDATE discounts SET sum = {new_sum} WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_sum_in_discounts_by_id(self, id):
        query = f"SELECT sum FROM discounts WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_all_records_by_foreign_keys(self):
        query = "SELECT discounts.id, customers.name, products.name, products.quantity, discounts.sum FROM discounts\
            JOIN customers ON discounts.customer_id = customers.id\
            JOIN orders ON discounts.order_id = orders.id\
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_all_records_by_sum(self, sum):
        records = self.get_discounts()
        found_sum = False

        for record in records:
            if record[3] == sum:
                found_sum = True
                break

        if not found_sum:
            raise ValueError(
                f"Discount with sum {sum} does not exist in the discounts table!"
            )

        query = f"SELECT discounts.id, customers.name, products.name, products.quantity, discounts.sum FROM discounts\
            JOIN customers ON discounts.customer_id = customers.id\
            JOIN orders ON discounts.order_id = orders.id\
            JOIN products ON orders.product_id = products.id WHERE sum = {sum}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def delete_record_by_id(self, id):
        query = f"DELETE FROM discounts WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_records_from_discounts(self):
        query = "DELETE FROM discounts"
        self.cursor.execute(query)
        self.connection.commit()

    def drop_table_discounts(self):
        query = f"DROP TABLE discounts"
        self.cursor.execute(query)
        self.connection.commit
