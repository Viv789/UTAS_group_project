import uuid
import boto3
import csv
import pandas as pd

def read_from_csv(filename):
    with open(filename, 'r') as myFile:
        return myFile.readlines()

def extract_from_csv(raw_data):
    csv_data = csv.reader(raw_data)
    df = pd.DataFrame(csv_data, columns=["date_time", "location", "customer_name", "basket", "payment_method", "total_price", "card_details"]) #reads csv file and assigns given headers
    return df

def extract_froms3(event):
    s3_event = event["Records"][0]["s3"]
    bucket = s3_event["bucket"]["name"]
    key = s3_event["object"]["key"]
    s3_resource = boto3.resource("s3")
    s3_object = s3_resource.Object(bucket, key)
    raw = s3_object.get()["Body"].read().decode("utf-8").splitlines()
    return raw


def extract(event):
    # raw_data = read_from_csv('./test_data.csv')
    raw_data = extract_froms3(event)
    df = extract_from_csv(raw_data)



    # df = pd.DataFrame(raw_data) #converts the csv into into a dataframe
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
