import unittest
import pandas as pd
from unittest.mock import Mock, patch, MagicMock
from pandas.testing import assert_frame_equal
from load import load_to_product, load_to_basket

@patch("load.query")
@patch("connection.psycopg2")
@patch("builtins.print")
def test_load_to_product(mock_query, mock_psycopg, mock_print): 
    
    mock_query.return_value = ({
        "product_id" : "c4ea45ec-275b-4421-8dcc-fa21d5151b27",
        "product_name": "hot chocolate",
        "size" : "large",
		"price" : "2.9"
    })	
    
    # assert load_to_product(df) == ({
    #     "product_id" : "c4ea45ec-275b-4421-8dcc-fa21d5151b27",
    #     "product_name": "hot chocolate",
    #     "size" : "large",
	# 	"price" : "2.9"
    # })

    mock_print.assert_called_with("data loaded to product table")


#load basket table
#@patch("load.a")
@patch("builtins.print")
def test_load_to_basket(mock_a):
    
    df= MagicMock
    
    mock_a.return_value = ({ "transaction_id" : "448eacd3-2a76-4d37-9a60-71c8d3f5cccb",
                            "product_id" : "c4ea45ec-275b-4421-8dcc-fa21d5151b27"
        })  		

    assert load_to_basket(df) == ({ "transaction_id" : "448eacd3-2a76-4d37-9a60-71c8d3f5cccb",
                                "product_id" : "c4ea45ec-275b-4421-8dcc-fa21d5151b27"
        })

    mock_print.assert_called_with("data loaded to basket table")

