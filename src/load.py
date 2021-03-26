import pandas as pd
from src.connection import connection
from uuid import uuid4



# load products table
def load_products(row, conn):
    cursor = conn.cursor()
    basket = row['basket']
    prod_ids = []
    for i, product in enumerate(basket):
        # ToDo: Check if exists first
        sql_query = "SELECT product_id FROM product WHERE product_name = %s AND size = %s"
        p_values = (str(product["name"]), str(product["size"]))
        cursor.execute(sql_query, p_values)
        result = cursor.fetchone()
        if result == None:
            sql_query = "INSERT INTO product (product_id, product_name, size, price) VALUES (%s, %s, %s, %s)"
            prod_ids.append(str(uuid4()))
            vals = list(product.values())
            vals.insert(0, prod_ids[i])
            cursor.execute(sql_query, tuple(vals))
            conn.commit()
        else:
            prod_ids.append(result[0])
    return prod_ids
    
    print("data loaded to product table")

# load location table
def load_location(row, conn):
    name = row['location']['name']
    loc_id = uuid4()
    cursor = conn.cursor()

    # ToDo: Check if exists first - DONE
    sql_query = "SELECT location_id FROM location WHERE location_name = %s"
    l_values = str(name)

    cursor.execute(sql_query, (l_values,))

    result = cursor.fetchone()
    if result == None:
        sql_query = "INSERT INTO location (location_id, location_name) VALUES (%s, %s)"
        value = (str(loc_id), name)
        cursor.execute(sql_query, value)
        conn.commit()
        return loc_id
    else:
        return result[0]

    print("data loaded to location table")

# load transactions table
def load_transaction(row, loc_id, conn):
    cursor = conn.cursor()
    transaction = row['transaction']
    trans_id = uuid4()
    timestamp = transaction['date_time']
    pay_method = transaction['payment_method']
    order_total = transaction["total"]
    sql_query = "INSERT INTO transaction (transaction_id, date_time, location_id, payment_method, order_total) VALUES (%s, %s, %s, %s, %s)"
    values = (str(trans_id), timestamp, str(loc_id), pay_method, order_total)
    cursor.execute(sql_query, values)
    conn.commit()
    return trans_id

    print("data loaded to transaction table")

# load basket table
def load_basket(row, trans_id, conn):
    cursor = conn.cursor()
    prod_ids = load_products(row, conn)
    for p_id in prod_ids:
        sql_query = "INSERT INTO basket (transaction_id, product_id) VALUES (%s, %s)"
        b_values = (str(trans_id), str(p_id))
        cursor.execute(sql_query, b_values)
        conn.commit()

    print("data loaded to basket table")

def load(raw):
    conn = connection()
    for row in raw:
        loc_id = load_location(row, conn)
        trans_id = load_transaction(row, loc_id, conn)
        load_basket(row, trans_id, conn)
    conn.close()