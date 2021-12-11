import unittest
from repositories.stock_repository import StockRepository
from database.init_db import initialize_db
from database.db_connection import get_connection


class TestStockRepository(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        initialize_db()
        self.user_id = 1
        self.repo = StockRepository(self.conn, self.user_id)

    def test_empty_data(self):
        result, _ = self.repo.get_user_data()
        print(result)
        self.assertEqual(len(result), 0)

    def test_add_correct_data(self):
        data = (self.user_id, "Microsoft", "MSFT", 100, 10, 300, "USD")
        result = self.repo.add_stock(data)
        self.assertEqual(result, True)

    def test_add_wrong_data(self):
        data1 = (self.user_id, "Microsoft", "MSFT", 100, 10, 300)
        result = self.repo.add_stock(data1)
        self.assertEqual(result, False)

    def test_add_get(self):
        data = (self.user_id, "Microsoft", "MSFT", 100, 10, 300, "USD")
        self.repo.add_stock(data)
        result, _ = self.repo.get_user_data()
        self.assertEqual(result[0][2], "Microsoft")

    def test_remove_stock(self):
        data = (self.user_id, "Microsoft", "MSFT", 100, 10, 300, "USD")
        self.repo.add_stock(data)
        result, _ = self.repo.get_user_data()
        self.assertEqual(result[0][2], "Microsoft")
        result2 = self.repo.remove_stock("MSFT")
        self.assertEqual(result2, True)
        result3, _ = self.repo.get_user_data()
        self.assertEqual(len(result3), 0)

    def test_get_tickers_empty(self):
        result, _ = self.repo.get_stock_tickers()
        self.assertEqual(len(result), 0)

    def test_get_tickers(self):
        data = (self.user_id, "Microsoft", "MSFT", 100, 10, 300, "USD")
        self.repo.add_stock(data)
        data = (self.user_id, "Apple", "AAPL", 10, 100, 400, "USD")
        self.repo.add_stock(data)
        result, _ = self.repo.get_stock_tickers()
        print(result)
        self.assertEqual(result[0][0], "MSFT")
        self.assertEqual(result[1][0], "AAPL")

    def test_get_one_stock(self):
        data = (self.user_id, "Microsoft", "MSFT", 100, 10, 300, "USD")
        self.repo.add_stock(data)
        result, success = self.repo.get_data_one_stock("MSFT")
        self.assertEqual(len(result[0]), len(data) + 1)
        self.assertEqual(success, True)
        self.assertEqual(result[0][2], data[1])
