import pandas as pd
from sqlalchemy import create_engine
import uuid
import psycopg2

csv_dataframe = pd.read_csv("2021-02-23-isle-of-wight (1).csv")
csv_dataframe = csv_dataframe.drop("customer_name", 1)
csv_dataframe = csv_dataframe.drop("card_details", 1)
csv_dataframe["uuid"] = [uuid.uuid4() for x in range(len(csv_dataframe.index))]

conn = psycopg2.connect(
    host="localhost", database="cafe_data", user="postgres", password="docker"
)
mycursor = conn.cursor()


def create_list_of_products(csv_dataframe):
    new_product_list = []

    for i in range(len(csv_dataframe)):
        order_string = csv_dataframe.loc[i, "basket"].lower()

        raw_order_list = order_string.split(",")
        for item in raw_order_list:
            if "." in item or (item == "large") or (item == "regular") or (item == ""):
                pass

            else:
                if (raw_order_list[(raw_order_list.index(item) - 1)]) == "large":
                    product_size = "large"
                else:
                    product_size = "regular"

                price = float(raw_order_list[(raw_order_list.index(item) + 1)])

                product_dictionary = {
                    "product": item,
                    "size": product_size,
                    "price": price,
                }

                if product_dictionary in new_product_list:
                    pass
                else:
                    new_product_list.append(product_dictionary)

    for x in new_product_list:
        product_id = str(uuid.uuid4())
        x["product_id"] = product_id

    cleaned_products_df = pd.DataFrame(new_product_list)

    print(cleaned_products_df)


def create_basket_list(csv_dataframe):
    list_of_baskets = []

    for i in range(len(csv_dataframe)):
        order_string = csv_dataframe.loc[i, "basket"].lower()
        order_id = csv_dataframe.loc[i, "uuid"]

        raw_order_list = order_string.split(",")
        for item in raw_order_list:
            if "." in item or (item == "large") or (item == "regular") or (item == ""):
                pass

            else:
                product_name = item
                product_price = price = float(
                    raw_order_list[(raw_order_list.index(item) + 1)]
                )
                a = "SELECT product_id from product WHERE product_name = %s AND price = %s"
                b = (product_name, product_price)
                mycursor.execute(a, b)
                product_id = mycursor.fetchone()[0]

                basket_dict = {"transaction_id": order_id, "product_id": product_id}
                list_of_baskets.append(basket_dict)

    return basket_dict


create_list_of_products(csv_dataframe)
