import sqlite3


class UserRepository:
    """Class for communicating with the database (table users).
    """

    def __init__(self, connection):
        """Constructor for the class.

        Args:
            connection (SQLite3 Connection): Connection for the database.
        """
        self.__connection = connection
        cursor = self.__connection.cursor()
        sql = """CREATE TABLE IF NOT EXISTS users (
        id integer primary key autoincrement, 
        username text UNIQUE, 
        password text);"""
        cursor.execute(sql)
        self.__connection.commit()

    def check_username_exists(self, username):
        """Checks if the given username exists.

        Args:
            username (string): Given username.

        Returns:
            boolean: Exists or does not.
        """
        cursor = self.__connection.cursor()
        sql = "SELECT username FROM users WHERE username=?"
        cursor.execute(sql, (username,))
        self.__connection.commit()
        rows = cursor.fetchall()
        return len(rows) > 0

    def correct_password(self, username, password):
        """Checks if the given username matches the given password.

        Args:
            username (string): Given usernname.
            password (string): Given password.

        Returns:
            boolean: If the username in the database has same password or not.
        """
        cursor = self.__connection.cursor()
        sql = "SELECT password FROM users WHERE username=?;"
        cursor.execute(sql, (username,))
        self.__connection.commit()
        user_password = cursor.fetchone()[0]
        return password == user_password

    def get_user_id(self, username):
        """Finds and returns the id of the given username.

        Args:
            username (string): Given username.

        Returns:
            integer: User id matching the given username.
        """
        cursor = self.__connection.cursor()
        sql = "SELECT id FROM users WHERE username=?;"
        cursor.execute(sql, (username,))
        self.__connection.commit()
        user_id = cursor.fetchone()[0]
        return user_id

    def add_user(self, username, password):
        """Method for adding a user to the database.

        Args:
            username (string): Username to be added.
            password (string): Password to be added.
        Returns:
            boolean: If the insertion is successful.
        """
        cursor = self.__connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (?, ?);"
        try:
            cursor.execute(sql, (username, password,))
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False

    def return_conn(self):
        """Returns the connection for the database.

        Returns:
            SQLite3 Connection: The connection for the database.
        """
        return self.__connection
