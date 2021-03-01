import pandas as pd
from sqlalchemy import create_engine
import psycopg2


raw_data = pd.read_csv("2021-02-23-isle-of-wight (1).csv")
raw_data = raw_data.drop("customer_name", 1)
raw_data = raw_data.drop("payment_info", 1)

engine = create_engine("postgresql://postgres:docker@localhost:5432/group_project")

raw_data.to_sql("group_table", engine)
