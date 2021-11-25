import unittest
from src.repositories.user_repository import UserRepository
from database.init_db import initialize_db
from database.db_connection import get_connection

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        conn = get_connection()
        initialize_db()
        self.repo = UserRepository(conn)

    