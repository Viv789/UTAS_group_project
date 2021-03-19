import uuid
import boto3
import pandas as pd

def extract_from_csv(csv_data):
    raw_data = pd.read_csv(csv_data, names=["datetime", "location", "customer_name", "basket", "payment_method", "total_price", "card_details"]) #reads csv file and assigns given headers
    return raw_data

def extract_froms3(event):
    s3_event = event["Records"][0]["s3"]
    bucket = s3_event["bucket"]["name"]
    key = s3_event["object"]["key"]
    s3_resource = boto3.resource("s3")
    s3_object = s3_resource.Object(bucket, key)
    raw = s3_object.get()["Body"].read().decode("utf-8").splitlines()
    return raw


def extract(event):
    raw_data = extract_from_csv('test_data.csv')
    # s3_data = extract_froms3(event)
    # raw_data = extract_from_csv(s3_data)



    df = pd.DataFrame(raw_data) #converts the csv into into a dataframe
    df.dropna(inplace = True) #Removes null values
    df.drop_duplicates() #Removes duplicates
    df.drop(df.columns[2], axis = 1, inplace = True) #Removes customer name 
    df.drop(df.columns[5], axis = 1, inplace = True) #Removes payment details
    return df


# def drop_sensitive_data(df):
#     df.drop(df.columns[2], axis = 1, inplace = True) #Removes customer name 
#     df.drop(df.columns[5], axis = 1, inplace = True) #Removes payment details
#     return df

# df = drop_sensitive_data(extract("./src/2021-02-23-isle-of-wight(1).csv"))
