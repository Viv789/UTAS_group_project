import unittest
from unittest.mock import MagicMock, patch

def test_create_tables():
    expected = ("CREATE TABLE product ("
            "product_id VARCHAR(255) NOT NULL,"
            "product_name VARCHAR(255) NOT NULL,"
            "size VARCHAR(255),"
            "price FLOAT,"
            "PRIMARY KEY (product_id))")
    
    mock_execute = MagicMock()
    
    result = test_create_tables()
    self.assertEqual(actual, expected)