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

# for order in list_of_orders:
#     for item in order:
#         if item == "Large" or "large":
#             product_dict = {
#                 "Size": "Large",
#                 "Product": order[order.index(item) + 1],
#                 "Price": order[order.index(item) + 2],
#             }
# #         else:
# #             product_dict = {
# #                 "Size": "Regular",
# #                 "Product": item,
# #                 "Price": order[order.index(item) + 1],
# #             }
# #     print(product_dict)

products = []
for order in list_of_orders:
    for x in order:
        if x == "Large" or "." in x:
            pass
        else:
            if x in products:
                pass
            else:
                product_dict = {
                    "Product Name": x,
                }
                # item_index = order.index(x)
                # if order[item_index - 1] == "Large":
                #     product_dict["Size"] = "Large"
            products.append(product_dict)

for x in products:
    print(x)
