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
            return []

    def add_stock(self, data):
        if len(data) == 5:    
            success = self.__repo.add_stock(data)
            return success
        else:
            return False
