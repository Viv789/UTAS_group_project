import unittest
from unittest.mock import MagicMock, patch
from pandas.testing import assert_frame_equal
from transform import create_location_list


def test_create_location_list():
    
    df = ({"datetime": "2021-02-23 09:00:48",
                    "location" : "Isle of Wight",
                    "item": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9", 
                    "payment_method": "CASH",
                    "total_price": "8.40"
    })
    
    expected = ({
        "location_id": "e6407dea-dd41-431e-9801-1d8751f65586",
        "location" : "Isle of Wight"
    })
    
    actual = create_location_list(df)
    
    assert_frame_equal(expected, actual)
