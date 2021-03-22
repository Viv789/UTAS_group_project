import pandas as pd
from src.connection import connection
from uuid import uuid4

conn = connection()
mycursor = conn.cursor() 
# load products table
def load_products(row):

    basket = row['basket']
    prod_ids = []

    for i, product in enumerate(basket):
        # ToDo: Check if exists first

        a = "SELECT product_id FROM product WHERE product_name = %s AND size = %s"
        b = (str(product["name"]), str(product["size"]))
        mycursor.execute(a, b)
        result = mycursor.fetchone()

        if result == None:
            query = "INSERT INTO product (product_id, product_name, size, price) VALUES (%s, %s, %s, %s)"
            prod_ids.append(str(uuid4()))
            vals = list(product.values())
            vals.insert(0, prod_ids[i])
            mycursor.execute(query, tuple(vals))
            conn.commit()
        else:
            prod_ids.append(result[0])
    return prod_ids


print("data loaded to product table")

# load location table


def load_location(row):

    name = row['location']['name']
    loc_id = uuid4()
    # ToDo: Check if exists first - DONE

    a = "SELECT location_id FROM location WHERE location_name = %s"
    b = str(name)
    mycursor.execute(a, (b,))
    result = mycursor.fetchone()

    if result == None:

        query = "INSERT INTO location (location_id, location_name) VALUES (%s, %s)"
        value = (str(loc_id), name)
        mycursor.execute(query, value)
        conn.commit()
        return loc_id

    else:
        return result[0]

    print("data loaded to location table")

# load transactions table


def load_transaction(row, loc_id):

    transaction = row['transaction']
    trans_id = uuid4()

    timestamp = transaction['timestamp']
    pay_method = transaction['payment_method']
    order_total = transaction["total"]

    query = "INSERT INTO transaction (transaction_id, datetime, location_id, payment_method, order_total) VALUES (%s, %s, %s, %s, %s)"

    values = (str(trans_id), timestamp, str(loc_id), pay_method, order_total)

    mycursor.execute(query, values)
    conn.commit()
    print("data loaded to transaction table")
    return trans_id

# load basket table


def load_basket(row, trans_id):

    prod_ids = load_products(row)

    for p_id in prod_ids:

        a = "INSERT INTO basket (transaction_id, product_id) VALUES (%s, %s)"
        b = (str(trans_id), str(p_id))
        mycursor.execute(a, b)
        conn.commit()
    print("data loaded to basket table")


def load(raw):
    for row in raw:
        loc_id = load_location(row)
        trans_id = load_transaction(row, loc_id)
        load_basket(row, trans_id)
