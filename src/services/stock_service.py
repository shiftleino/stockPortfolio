import yfinance as yf
from repositories.stock_repository import StockRepository
import pandas as pd

class StockService:
    def __init__(self, user_id, conn):
        self.__user_id = user_id
        self.__conn = conn
        self.__repo = StockRepository(self.__conn, self.__user_id)

    def return_user_data(self):
        data, success = self.__repo.get_user_data()
        if success:
            return data
        return ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]

    def add_stock(self, name, ticker, amount, buy_price):
        current, currency, success1 = self.get_stock_price(ticker)
        data = (self.__user_id, name, ticker,
                amount, buy_price, current, currency)
        user_stocks, success2 = self.return_stock_tickers()
        if success1 and success2:
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
            return current, currency, True
        except:
            return 0, "N/A", False

    def remove_stock(self, ticker):
        success = self.__repo.remove_stock(ticker)
        return success

    def return_stock_tickers(self):
        tickers, success = self.__repo.get_stock_tickers()
        result = [ticker for t in tickers for ticker in t]
        return result, success

    def check_if_ticker_in_db(self, ticker):
        result, success = self.__repo.get_stock_tickers()
        tickers = [ticker for t in result for ticker in t]
        if success:
            if ticker in tickers:
                return True
            else:
                return False
        else:
            return True

    def get_data_of_stock(self, ticker):
        result, success = self.__repo.get_data_one_stock(ticker)
        if success:
            return result[0]
        else:
            return ("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
    
    def get_historical_data(self, ticker):
        try:
            data = yf.download(tickers=ticker, period="max")
            x = data.index.to_pydatetime()
            y = data["Adj Close"]
            return [i.timestamp() for i in x], y
        except:
            return [], []
