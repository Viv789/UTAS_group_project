import numpy as np
import pandas as pd

filename = 'isle.csv'
df = pd.read_csv(filename)
# print(df.head())

df.drop('customer_info', axis=1, inplace=True) 
df.drop('card_details', axis=1, inplace=True)
print(df.head())