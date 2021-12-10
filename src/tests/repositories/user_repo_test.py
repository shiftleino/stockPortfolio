import unittest
from repositories.user_repository import UserRepository
from database.init_db import initialize_db
from database.db_connection import get_connection


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        initialize_db()
        self.repo = UserRepository(self.conn)

    def test_add_user(self):
        first = self.repo.add_user("username1", "1234")
        self.assertEqual(first, True)
        second = self.repo.add_user("username1", "4321")
        self.assertEqual(second, False)
        self.conn.close()

    def test_return_conn(self):
        conn = self.repo.return_conn()
        self.assertEqual(conn, self.conn)
        self.conn.close()

    def test_get_user_id(self):
        self.repo.add_user("username1", "1234")
        id_ = self.repo.get_user_id("username1")
        self.assertEqual(id_, 1)
        self.conn.close()

    def test_correct_password(self):
        self.repo.add_user("username1", "1234")
        result = self.repo.correct_password("username1", "1234")
        self.assertEqual(result, True)
        self.conn.close()

    def test_wrong_password(self):
        self.repo.add_user("username1", "1234")
        result = self.repo.correct_password("username1", "4321")
        self.assertEqual(result, False)
        self.conn.close()

    def test_username_exists(self):
        self.repo.add_user("username1", "1234")
        result = self.repo.check_username_exists("username1")
        self.assertEqual(result, True)
        self.conn.close()

    def test_username_not_exists(self):
        self.repo.add_user("username1", "1234")
        result = self.repo.check_username_exists("username2")
        self.assertEqual(result, False)
        self.conn.close()
