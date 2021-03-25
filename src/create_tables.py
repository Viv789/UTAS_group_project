

'''
SQL Script for Db tables
'''

#For connection to Postgre db
from connection import *

''' 
Ensure that you have created a cafe_data database first, then run this
'''

# create_tables

def create_tables():
    engine.execute(CREATE TABLE IF NOT EXISTS product (
                product_id VARCHAR(255) NOT NULL PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                size VARCHAR(255),
                price FLOAT
            );

    engine.execute(CREATE TABLE IF NOT EXISTS location (
                location_id VARCHAR(255) NOT NULL PRIMARY KEY,
                location_name VARCHAR(255)
            );

    engine.execute(CREATE TABLE IF NOT EXISTS transaction (
                transaction_id VARCHAR(255) NOT NULL PRIMARY KEY,
                date_time  timestamp NOT NULL,
                location_id  VARCHAR(255) NOT NULL,
                payment_method VARCHAR(255) NOT NULL,
                order_total FLOAT,
                FOREIGN KEY (location_id) REFERENCES location (location_id))
            );

    engine.execute(CREATE TABLE IF NOT EXISTS basket (
                transaction_id VARCHAR(255) NOT NULL,
                product_id  VARCHAR(255) NOT NULL,
                CONSTRAINT fk_basket
                FOREIGN KEY (transaction_id) REFERENCES transaction (transaction_id),
                FOREIGN KEY (product_id) REFERENCES product (product_id)
            );

# To check if database is empty
def database_is_empty():
    table_names = sa.inspect(engine).get_table_names()
    is_empty = table_names == []
    print('Db cafe_data is empty: {}'.format(is_empty))
    return is_empty

# To check if all tables were created 
def table_exists(name):
    exist = engine.dialect.has_table(engine, name)
    print('Table {} exists: {}'.format(name, exist))
    return exist

#Call tables
def tables():
    names = ['product', 'location', 'transaction', 'basket']
    for name in names:
        table_exists(name)

#Call database to ensure it exists
#database_is_empty()

#Create tables
#create_tables()

#Call tables
#tables()