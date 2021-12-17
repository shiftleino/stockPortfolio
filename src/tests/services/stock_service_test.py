import unittest
from services.stock_service import StockService
from database.init_db import initialize_db
from database.db_connection import get_connection


class TestStockService(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        initialize_db()
        self.user_id = 1
        self.service = StockService(self.user_id, self.conn)

    def test_return_data_empty(self):
        result = self.service.return_user_data()
        self.assertEqual(len(result), 0)

    def test_return_user_data(self):
        result1 = self.service.add_stock("Tesla", "TSLA", 30, 300)
        result2 = self.service.add_stock("Apple", "AAPL", 11, 52)
        self.assertEqual(result1 & result2, True)
        data = self.service.return_user_data()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][3], "TSLA")

    def test_add_wrong_stock(self):
        result1 = self.service.add_stock("NotRealStock", "1234", 30, 300)
        self.assertEqual(result1, False)
        result2 = self.service.add_stock("Tesla", "TSLA", 30, 300)
        self.assertEqual(result2, True)
        result3 = self.service.add_stock("Tesla", "TSLA", 30, 300)
        self.assertEqual(result3, False)

    def test_stock_price(self):
        price, currency, result = self.service.get_stock_price("MSFT")
        self.assertEqual(type(price), float)
        self.assertEqual(currency, "USD")
        self.assertEqual(result, True)

    def test_remove_stock(self):
        result1 = self.service.add_stock("Tesla", "TSLA", 30, 300)
        self.assertEqual(result1, True)
        data = self.service.return_user_data()
        self.assertEqual(len(data), 1)
        result2 = self.service.remove_stock("TSLA")
        self.assertEqual(result2, True)
        data = self.service.return_user_data()
        self.assertEqual(len(data), 0)

    def test_return_tickers(self):
        result1 = self.service.add_stock("Tesla", "TSLA", 30, 300)
        result2 = self.service.add_stock("Apple", "AAPL", 11, 52)
        if result1 & result2:
            tickers, result3 = self.service.return_stock_tickers()
            self.assertEqual(result3, True)
            self.assertEqual(tickers[0], "TSLA")
            self.assertEqual(tickers[1], "AAPL")
            self.assertEqual(len(tickers), 2)

    def test_check_ticker(self):
        result1 = self.service.check_if_ticker_in_db("MSFT")
        self.assertEqual(result1, False)
        self.service.add_stock("Microsoft", "MSFT", 21, 121)
        result2 = self.service.check_if_ticker_in_db("MSFT")
        self.assertEqual(result2, True)

    def test_get_data(self):
        self.service.add_stock("Tesla", "TSLA", 20, 120)
        data2 = self.service.get_data_of_stock("TSLA")
        self.assertEqual(data2[5], 120)

    def test_get_historical_data(self):
        x_values, y_values = self.service.get_historical_data("AAPL")
        self.assertEqual(len(x_values) == len(y_values), True)

    def test_get_data_sorted(self):
        self.service.add_stock("Tesla", "TSLA", 20, 120)
        self.service.add_stock("Microsoft", "MSFT", 21, 121)
        self.service.add_stock("Apple", "AAPL", 11, 52)
        data = self.service.return_user_data()
        self.assertEqual(data[0][3], "TSLA")
        sorted_data = self.service.get_data_sorted("Stock")
        self.assertEqual(sorted_data[0][3], "AAPL")
