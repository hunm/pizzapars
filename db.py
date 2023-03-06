import psycopg2


class DatBase:

    def __init__(self):
        self.connection = psycopg2.connect(database='pizzamia',
                                           user='pizzamia',
                                           password='pizzamia',
                                           host='localhost',
                                           port='6432')
        self.cursor = self.connection.cursor()

    def create_tables(self) -> None:
        """create tables in the database."""
        with open("bot/sql/init.sql", "r") as f:
            sql = f.read()
        self.cursor.execute(sql)
        self.connection.commit()

    def add_category(self, category_name) -> None:
        """add category in the database"""
        query = "INSERT INTO Categories (category_name) values (%s)"
        self.cursor.execute(query, category_name)
        self.connection.commit()

    def add_product(self, category_id, product_name, product_description, product_price):
        """add product in the database"""
        query = "INSERT INTO Categories (category_id, product_name, product_description, product_price) values (%s, " \
                "%s, %s, %s) "
        self.cursor.execute(query, category_id, product_name, product_description, product_price)
        self.connection.commit()

    def get_category_by_id(self, category_id) -> str:
        """get category name from the database"""
        query = "SELECT category_name FROM Categories WHERE id = %s"
        self.cursor.execute(query, str(category_id))
        return self.cursor.fetchall()
