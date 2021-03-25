import numpy as np
import time


def transform_location(row: list):
    return {"name": row[1].upper()}


def transform_transaction(row: list):
    epoch = int(time.mktime(time.strptime(row[0], "%Y-%m-%d %H:%M:%S")))
    return {"date_time": epoch, "total": row[4], "payment_method": row[3]}


def transform_basket(row: list):
    basket = []
    items = row[2].split(",")

    def chunked(l: list, n: int):
        return np.array_split(l, n)

    def build_item(size: str, name: str, price: float):
        return {"size": size.upper(), "name": name.upper(), "price": price}

    chunks = chunked(items, int(len(items) / 3))

    for chunk in chunks:
        basket.append(build_item(chunk[0], chunk[1], chunk[2]))

    return basket


def transform_row(row: list):

    location = transform_location(row)
    transaction = transform_transaction(row)
    basket = transform_basket(row)

    return {"location": location, "basket": basket, "transaction": transaction}


def transform(raw: list):
    transformed = []
    for row in raw:
        transformed.append(transform_row(row))
    return transformed
