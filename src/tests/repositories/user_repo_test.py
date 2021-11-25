import unittest
from repositories.user_repository import UserRepository
from database.init_db import initialize_db
from database.db_connection import get_connection

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        conn = get_connection()
        initialize_db()
        self.repo = UserRepository(conn)

    def test_add_user(self):
        first = self.repo.add_user("username1", "1234")
        self.assertEqual(first, True)
        second = self.repo.add_user("username1", "4321")
        self.assertEqual(second, False)