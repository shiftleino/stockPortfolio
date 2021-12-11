import sqlite3


class StockRepository:
    """Class for the communication with the database (table stocks).
    """
    def __init__(self, connection, user_id):
        """Constructor for the StockRepository class.
        
        Args:
            connection (SQLite3 Connection): The connection for the database.
            user_id (integer): User's id.
        """
        self.__connection = connection
        self.user_id = user_id
        self.__cursor = self.__connection.cursor()
        sql = """CREATE TABLE IF NOT EXISTS stocks (
        id integer primary key autoincrement, 
        user_id integer,
        name text,
        ticker text,
        amount integer,
        price real,
        current real,
        currency text);"""
        self.__cursor.execute(sql)
        self.__connection.commit()

    def get_user_data(self):
        """Method for getting all the user's stocks.

        Returns:
            list, boolean: Returns the data of the user and if this was successful.
        """
        try:
            sql = "SELECT * FROM stocks WHERE user_id=?;"
            self.__cursor.execute(sql, (self.user_id,))
            self.__connection.commit()
            data = self.__cursor.fetchall()
            return data, True
        except sqlite3.Error:
            return [], False

    def add_stock(self, data):
        """Method for adding a stock to the database.
        
        Args:
            data (list): The data of the stock to be added.
        
        Returns:
            boolean: If the method was successfully completed.
        """
        try:
            sql = """INSERT INTO stocks 
            (user_id, name, ticker, amount, price, current, currency) 
            VALUES (?,?,?,?,?,?,?);"""
            self.__cursor.execute(sql, data)
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False

    def remove_stock(self, ticker):
        """Removes a stock from the database.

        Args:
            ticker (string): The ticker of the stock to be removed.

        Returns:
            boolean: If this method was successful or not.
        """
        try:
            sql = "DELETE FROM stocks WHERE user_id=? AND ticker=?;"
            self.__cursor.execute(sql, (self.user_id, ticker))
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False

    def get_stock_tickers(self):
        """Method for getting all the tickers of the given user.

        Returns:
            list, boolean: The list of the tickers and if the method was successful.
        """
        try:
            sql = "SELECT ticker FROM stocks WHERE user_id=?;"
            self.__cursor.execute(sql, (self.user_id,))
            self.__connection.commit()
            data = self.__cursor.fetchall()
            return data, True
        except sqlite3.Error:
            return [], False

    def get_data_one_stock(self, ticker):
        """Method for getting all the data in the database for one stock.

        Args:
            ticker (string): The ticker of the stock whose data is wanted.

        Returns:
            list, boolean: The data of the stock and if this method was successful or not.
        """
        try:
            sql = "SELECT * FROM stocks WHERE user_id=? AND ticker=?;"
            self.__cursor.execute(sql, (self.user_id, ticker))
            self.__connection.commit()
            data = self.__cursor.fetchall()
            return data, True
        except sqlite3.Error:
            return [], False
