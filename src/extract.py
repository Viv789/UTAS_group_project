import uuid
import pandas as pd

def extract(file_name):
    raw_data = pd.read_csv(file_name, names=["datetime", "location", "customer_name", "basket", "payment_method", "total_price", "card_details"]) #reads csv file and assigns given headers
    df = pd.DataFrame(raw_data) #converts the csv into into a dataframe
    df.dropna(inplace = True) #Removes null values
    df.drop_duplicates() #Removes duplicates
    return raw_data


def drop_sensitive_data(df):
    df.drop(df.columns[2], axis = 1, inplace = True) #Removes customer name 
    df.drop(df.columns[5], axis = 1, inplace = True) #Removes payment details
    return df

df = drop_sensitive_data(extract("./src/2021-02-23-isle-of-wight.csv"))
