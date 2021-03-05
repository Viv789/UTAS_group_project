import psycopg2
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:docker@localhost:5432/cafe_data")
engine.connect()

engine.execute('CREATE TABLE product ('
            'product_id VARCHAR(255) NOT NULL,'
            'product_name VARCHAR(255) NOT NULL,'
            'size VARCHAR(255),'
            'price FLOAT,'
            'PRIMARY KEY (product_id))'
        );
engine.execute('CREATE TABLE location ('
            'location_id VARCHAR(255) NOT NULL,'
            'location_name VARCHAR(255),'
            'PRIMARY KEY (location_id))'
        );
engine.execute('CREATE TABLE transaction ('
            'transaction_id VARCHAR(255) NOT NULL,'
            'datetime VARCHAR(255) NOT NULL,'
            'location_id  VARCHAR(255) NOT NULL,'
            'payment_method VARCHAR(255) NOT NULL,'
            'order_total FLOAT,'
            'PRIMARY KEY (transaction_id),'
            'FOREIGN KEY (location_id) REFERENCES location (location_id))'
        );
engine.execute('CREATE TABLE basket ('
            'basket_id INT NOT NULL, '
            'transaction_id VARCHAR(255) NOT NULL,'
            'product_id  VARCHAR(255) NOT NULL,'
            'PRIMARY KEY (basket_id),'
            'FOREIGN KEY (transaction_id) REFERENCES transaction (transaction_id),'
            'FOREIGN KEY (product_id) REFERENCES product (product_id))'
        );





