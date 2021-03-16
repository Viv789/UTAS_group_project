from src.extract import extract, drop_sensitive_data
from src.load import load
from src.transform import transform

def main_extract(file_name):
    df = drop_sensitive_data(extract(file_name))
    return df

def main_transform(df):
    return transform(df.values.tolist())


def pipe(f_name):
    raw = main_extract(f_name)
    transformed = main_transform(raw)
    #print(transformed)
    load(transformed)


pipe("./src/2021-02-23-isle-of-wight.csv")