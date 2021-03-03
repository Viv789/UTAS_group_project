import pandas as pd
from sqlalchemy import create_engine
import psycopg2


raw_data = pd.read_csv("2021-02-23-isle-of-wight (1).csv")
# raw_data = raw_data.drop("customer_name", 1)
# raw_data = raw_data.drop("payment_info", 1)

# engine = create_engine("postgresql://postgres:docker@localhost:5432/group_project")

# raw_data.to_sql("group_table2", engine)

list_of_orders = []
for x in range(539):
    v = (raw_data["order"].loc[x]).split(",")
    for i in v:
        if i == "":
            v.remove(i)
    list_of_orders.append(v)


products = []
for order in list_of_orders:
    for item in order:
        if item == "Large" or "." in item or "Regular" in item:
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
            if "." in order[price_loc]:
                product_dict = {"Product": x, "Price": float(order[price_loc])}
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

for r in clean_list_of_product_dicts:
    for f in clean_list_of_product_dicts:
        if (r["Product"] == f["Product"]) and r["Price"] != f["Price"]:
            print(r, f)