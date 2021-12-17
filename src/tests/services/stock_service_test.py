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
