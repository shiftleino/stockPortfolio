from repositories.stock_repository import StockRepository
import yfinance as yf

class StockService:
    def __init__(self, user_id, conn):
        self.__user_id = user_id
        self.__conn = conn
        self.__repo = StockRepository(self.__conn, self.__user_id)

    def return_user_data(self):
        data, success = self.__repo.get_user_data()
        if success:
            return data
        return ["N/A", "N/A", "N/A", "N/A", "N/A"]

    def add_stock(self, name, ticker, amount, buy_price):
        data = (self.__user_id, name, ticker, amount, buy_price)
        user_stocks, success1 = self.return_stock_tickers()
        if success1:
            if ticker not in user_stocks:
                success = self.__repo.add_stock(data)
                return success
            else: 
                return False
        else:
            return False

    def get_stock_price(self, ticker):
        try:
            ticker = yf.Ticker(ticker)
            current = ticker.info["currentPrice"]
            currency = ticker.info["financialCurrency"]
            return 0, "EUR", True
        except:
            return 0, "N/A", False

    def remove_stock(self, ticker):
        success = self.__repo.remove_stock(ticker)
        return success

    def return_stock_tickers(self):
        tickers, success = self.__repo.get_stock_tickers()
        result = [ticker for t in tickers for ticker in t]
        return result, success