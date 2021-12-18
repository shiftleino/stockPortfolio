import unittest
from services.user_service import UserService
from database.init_db import initialize_db
from database.db_connection import get_connection


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        initialize_db()
        self.service = UserService(self.conn)

    def test_login_user(self):
        username = "username"
        password = "1234"
        password_wrong = "false"
        result1 = self.service.login(username, password)
        self.assertEqual(result1, False)
        self.service.add_user(username, password)
        result2 = self.service.login(username, password_wrong)
        self.assertEqual(result2, False)
        result3 = self.service.login(username, password)
        self.assertEqual(result3, True)

    def test_get_id(self):
        username = "username"
        password = "1234"
        self.service.add_user(username, password)
        user_id = self.service.get_id(username)
        self.assertEqual(user_id, 1)

    def test_user(self):
        username = "username"
        password = "1234"
        user_id = 1
        self.service.set_username(username)
        self.service.set_password(password)
        self.service.set_id(user_id)
        result1 = self.service.return_id()
        result2 = self.service.return_password()
        result3 = self.service.return_username()
        self.assertEqual(result1, user_id)
        self.assertEqual(result2, password)
        self.assertEqual(result3, username)
