import pandas as pd
from sqlalchemy import create_engine
import psycopg2


raw_data = pd.read_csv("2021-02-23-isle-of-wight (1).csv")
raw_data = raw_data.drop("customer_name", 1)
raw_data = raw_data.drop("payment_info", 1)

# engine = create_engine("postgresql://postgres:docker@localhost:5432/group_project")

# raw_data.to_sql("transaction", engine)

list_of_orders = []
for x in range(len(raw_data.index)):
    raw_string = (raw_data["order"].loc[x]).lower()
    v = raw_string.split(",")
    list_of_orders.append(v)


products = []
for order in list_of_orders:
    for item in order:
        if item == "large" or "." in item or "regular" in item:
            pass
        else:
            if item in products:
                pass
            else:
                products.append(item)

raw_list_of_product_dicts = []
for order in list_of_orders:
    for x in products:
        if x in order:
            price_loc = order.index(x) + 1
            size_loc = order.index(x) - 1
            if "." in order[price_loc]:
                product_dict = {"Product": x, "Price": float(order[price_loc])}
                if order[size_loc] == "large":
                    product_dict["Size"] = "large"
                elif order[size_loc] == "" or "regular":
                    product_dict["Size"] = "regular"
                raw_list_of_product_dicts.append(product_dict)
            else:
                pass


seen = set()
clean_list_of_product_dicts = []
for d in raw_list_of_product_dicts:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        clean_list_of_product_dicts.append(d)


conn = psycopg2.connect(
    host="localhost", database="group_project", user="postgres", password="docker"
)

mycursor = conn.cursor()


def insert_products_into_sql():
    for x in clean_list_of_product_dicts:
        name = x["Product"]
        size = x["Size"]
        price = x["Price"]
        a = "INSERT INTO product(product_name,product_size,price) VALUES (%s, %s, %s)"
        b = (name, size, price)
        mycursor.execute(a, b)
        conn.commit()


list_of_baskets = []
for order in list_of_orders:
    order_products = []
    for item in order:
        if item == "large" or item == "regular" or item == "" or ("." in item):
            pass
        else:
            order_products.append(item)
            # print(order_products)
    list_of_baskets.append(order_products)


# for order in list_of_orders:
#     for item in order:
#         if item == "large" or item == "regular" or item == "" or ("." in item):
#             pass
#         else:
#             transaction


print(raw_data["order"].str.lower().head(10))

