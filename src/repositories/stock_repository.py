class StockRepository:
    def __init__(self, connection, user_id):
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
        try:
            sql = "SELECT * FROM stocks WHERE user_id=?;"
            self.__cursor.execute(sql, (self.user_id,))
            self.__connection.commit()
            data = self.__cursor.fetchall()
            return data, True
        except:
            return [], False

    def add_stock(self, data):
        try:
            sql = "INSERT INTO stocks (user_id, name, ticker, amount, price, current, currency) VALUES (?,?,?,?,?,?,?);"
            self.__cursor.execute(sql, data)
            self.__connection.commit()
            return True
        except:
            return False

    def remove_stock(self, ticker):
        try:
            sql = "DELETE FROM stocks WHERE user_id=? AND ticker=?;"
            self.__cursor.execute(sql, (self.user_id, ticker))
            self.__connection.commit()
            return True
        except:
            return False

    def get_stock_tickers(self):
        try:
            sql = "SELECT ticker FROM stocks WHERE user_id=?;"
            self.__cursor.execute(sql, (self.user_id,))
            self.__connection.commit()
            data = self.__cursor.fetchall()
            return data, True
        except:
            return [], False