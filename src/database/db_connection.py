import sqlite3
from config import DB_PATH


def get_connection():
    """Creates a connection to the database.

    Returns:
        SQLite3 Connection: The connection to the database.
    """
    conn = sqlite3.connect(DB_PATH)
    return conn
