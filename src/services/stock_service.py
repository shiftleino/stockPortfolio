import sys
sys.path.append("src/repositories")
from stock_repository import StockRepository

class StockService:
    def __init__(self, user_id, conn):
        self.__user_id = user_id
        self.__conn = conn
        self.__repo = StockRepository(self.__conn, self.__user_id)

    def return_user_data(self):
        data, success = self.__repo.get_user_data()
        if success:
            return data
        else:
            return ["N/A", "N/A", "N/A", "N/A", "N/A"]

    def add_stock(self, name, ticker, amount, buy_price):
        data = (self.__user_id, name, ticker, amount, buy_price)    
        success = self.__repo.add_stock(data)
        return success

    def get_stock_price(self, ticker):
        return 0