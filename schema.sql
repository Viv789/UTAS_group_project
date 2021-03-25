drop table location, product, transaction, basket cascade;

CREATE TABLE IF NOT EXISTS product (
  product_id VARCHAR(255) NOT NULL PRIMARY KEY,
  product_name VARCHAR(255) NOT NULL,
  size VARCHAR(255),
  price FLOAT
);
CREATE TABLE IF NOT EXISTS location (
  location_id VARCHAR(255) NOT NULL PRIMARY KEY,
  location_name VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS transaction (
  transaction_id VARCHAR(255) NOT NULL PRIMARY KEY,
  date_time INT NOT NULL,
  location_id VARCHAR(255) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  order_total FLOAT,
  FOREIGN KEY (location_id) REFERENCES location (location_id)
);
CREATE TABLE IF NOT EXISTS basket (
  transaction_id VARCHAR(255) NOT NULL,
  product_id  VARCHAR(255) NOT NULL,
  CONSTRAINT fk_basket
  FOREIGN KEY (transaction_id) REFERENCES transaction (transaction_id),
  FOREIGN KEY (product_id) REFERENCES product (product_id)
);