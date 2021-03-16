import pandas as pd
from extract import drop_sensitive_data
from pandas.testing import assert_frame_equal

def test_drop_sensitive_data():
    
    df = pd.DataFrame({
        "datetime": ["2021-02-23 09:00:48"],
        "location" : ["Isle of Wight"],
        "customer_name": ["Morgan Berka"],
        "item": ["Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9"], 
        "payment_method": ["CASH"],
        "total_price": ["8.40"], 
        "card_details": ["None"]
    })  

    expected = pd.DataFrame({"datetime": ["2021-02-23 09:00:48"],
                    "location" : ["Isle of Wight"],
                    "item": ["Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9"], 
                    "payment_method": ["CASH"],
                    "total_price": ["8.40"]
    }) 
    
    actual = drop_sensitive_data(df)
    
    assert_frame_equal(expected, actual)
