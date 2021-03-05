import pandas as pd

def extract(file_name):
    raw_data = pd.read_csv(file_name, headers=["datetime", "location", "name", "item", "payment_method", "total_price", "card_details"]) #reads csv file and assigns given headers
    df = pd.DataFrame(raw_data) #converts the csv into into a dataframe
    df.dropna(inplace = True) #Removes null values
    df.drop_duplicates() #Removes duplicates 
    return df

def drop_sensitive_data(df):
    df.drop(df.columns[2], axis = 1, inplace = True) #Removes cust name 
    df.drop(df.columns[5], axis = 1, inplace = True) #Removes payment details
    return df


