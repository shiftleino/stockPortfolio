import sys
sys.path.append("src/entities")
from user import User
import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "username1234", "1234")

    def test_return_id(self):
        id = self.user.return_id()
        self.assertEqual(id, 1)
    
    def test_return_username(self):
        username = self.user.return_username()
        self.assertEqual(username, "username1234")
    
    def test_return_password(self):
        pw = self.user.return_password()
        self.assertEqual(pw, "1234")

    def test_set_username(self):
        self.user.set_username("username_new")
        self.assertEqual(self.user.return_username(), "username_new")

    def test_set_password(self):
        self.user.set_password("4321")
        self.assertEqual(self.user.return_password(), "4321")

    def test_set_id(self):
        self.user.set_id(2)
        self.assertEqual(self.user.return_id(), 2)
