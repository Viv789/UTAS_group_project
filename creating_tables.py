# For connection to Postgre db
import psycopg2
import sqlalchemy as sa
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:docker@localhost:5432/cafe_data")
engine.connect()

# Create Database
""" 
Ensure that you have created a cafe_data database first, then run this
"""

# create_tables
def create_tables():
    engine.execute(
        "CREATE TABLE product ("
        "product_id VARCHAR(255) NOT NULL,"
        "product_name VARCHAR(255) NOT NULL,"
        "size VARCHAR(255),"
        "price FLOAT,"
        "PRIMARY KEY (product_id))"
    )

    engine.execute(
        "CREATE TABLE location ("
        "location_id VARCHAR(255) NOT NULL,"
        "location_name VARCHAR(255),"
        "PRIMARY KEY (location_id))"
    )

    engine.execute(
        "CREATE TABLE transaction ("
        "transaction_id VARCHAR(255) NOT NULL,"
        "datetime  VARCHAR(255) NOT NULL,"
        "location_id  VARCHAR(255) NOT NULL,"
        "payment_method VARCHAR(255) NOT NULL,"
        "order_total FLOAT,"
        "PRIMARY KEY (transaction_id),"
        "FOREIGN KEY (location_id) REFERENCES location (location_id))"
    )

    engine.execute(
        "CREATE TABLE basket ("
        "basket_id INT NOT NULL, "
        "transaction_id VARCHAR(255) NOT NULL,"
        "product_id  VARCHAR(255) NOT NULL,"
        "PRIMARY KEY (basket_id),"
        "FOREIGN KEY (transaction_id) REFERENCES transaction (transaction_id),"
        "FOREIGN KEY (product_id) REFERENCES product (product_id))"
    )


# To check if database is empty
def database_is_empty():
    table_names = sa.inspect(engine).get_table_names()
    is_empty = table_names == []
    print("Db is empty: {}".format(is_empty))
    return is_empty


# To check if all tables were created
def table_exists(name):
    ret = engine.dialect.has_table(engine, name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret


# Call database to ensure it exists
database_is_empty()

# Create tables
create_tables()

# Call tables
names = ["product", "location", "transaction", "basket"]
for name in names:
    table_exists(name)