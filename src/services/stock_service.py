import yfinance as yf
import numpy as np
from repositories.stock_repository import StockRepository


class StockService:
    """Class for the application logic and 
    communcation between stock data storages and UI.
    """

    def __init__(self, user_id, conn):
        """Constructor for the StockService class.

        Args:
            user_id (integer): The id of the user.
            conn (SQLite3 Connection): Connection for the database.
        """
        self.__user_id = user_id
        self.__conn = conn
        self.__repo = StockRepository(self.__conn, self.__user_id)

    def return_user_data(self):
        """Method for getting the data of the user.

        Returns:
            list: List of lists of the data
        """
        data, success = self.__repo.get_user_data()
        if success:
            return data
        return [["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]]

    def add_stock(self, name, ticker, amount, buy_price):
        """Method for adding the data to the database.

        Args:
            name (string): Name of the stock.
            ticker (string): Ticker of the stock.
            amount (integer): Amount of the stocks.
            buy_price (float): The price the stock was bought.

        Returns:
            boolean: If the stock was successfully added or not.
        """
        current, currency, success1 = self.get_stock_price(ticker)
        data = (self.__user_id, name, ticker,
                amount, buy_price, current, currency)
        user_stocks, success2 = self.return_stock_tickers()
        if success1 and success2:
            if ticker not in user_stocks:
                success = self.__repo.add_stock(data)
                return success
            return False
        return False

    def get_stock_price(self, ticker):
        """Method for getting the current price of the stock.

        Args:
            ticker (string): The ticker of the stock.

        Returns:
            integer, string, boolean: The current price, 
            what currency the price is in 
            and whether the method was successful or not.
        """
        try:
            ticker = yf.Ticker(ticker)
            current = ticker.info["currentPrice"]
            currency = ticker.info["financialCurrency"]
            return current, currency, True
        except:
            return 0, "N/A", False

    def remove_stock(self, ticker):
        """Method for removing the stock from the database.

        Args:
            ticker (string): The ticker of the stock to be removed.

        Returns:
            boolean: If the method was successful or not.
        """
        success = self.__repo.remove_stock(ticker)
        return success

    def return_stock_tickers(self):
        """Method for getting the tickers of the stocks that user has.

        Returns:
            list, boolean: List of the tickers and if the method was successful.
        """
        tickers, success = self.__repo.get_stock_tickers()
        result = [ticker for t in tickers for ticker in t]
        return result, success

    def check_if_ticker_in_db(self, ticker):
        """Method for checking if the user has the ticker in her/his stocks.

        Args:
            ticker (string): The ticker of the stock.

        Returns:
            boolean: If the stock was in the database or not. 
            Return true also when the method is not successful 
            as an error message is then shown for the user.
        """
        result, success = self.__repo.get_stock_tickers()
        tickers = [ticker for t in result for ticker in t]
        if success:
            if ticker in tickers:
                return True
            return False
        return True

    def get_data_of_stock(self, ticker):
        """Method for getting data for one stock.

        Args:
            ticker (string): The ticker of the stock.

        Returns:
            list: The data for one stock.
        """
        result, success = self.__repo.get_data_one_stock(ticker)
        if success:
            return result[0]
        return ("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    def get_historical_data(self, ticker):
        """Method for getting all the historical data for the stock.

        Args:
            ticker (string): The ticker of the stock.

        Returns:
            list, list: Two lists, first one containing the 
            timestamps of the data and second one containing
            the historical stock prices. 
        """
        try:
            data = yf.download(tickers=ticker, period="max")
            x_values = data.index.to_pydatetime()
            y_values = data["Adj Close"]
            return [i.timestamp() for i in x_values], y_values
        except:
            return [], []

    def get_data_sorted(self, method):
        """Returns the data sorted by the chosen method.

        Args:
            method (string): The parameter to order the data.

        Returns:
            list: The sorted data (list of lists).
        """
        data, success = self.__repo.get_user_data()
        if success:
            transformed_data = []
            for stock in data:
                transformed_data.append((stock[0], stock[1], stock[2], stock[3], stock[4], stock[5], stock[6], stock[7], ((
                    stock[6] - stock[5]) / stock[5]) * 100, (stock[6] - stock[5])*stock[4]))
            dtype = [('Id', int), ('Userid', int), ('Stock', "<U100"), ('Ticker', "<U100"), ('Amount', int), (
                'Purchase Price', float), ('Current Price', float), ('Currency', "<U10"), ('Return-%', float), ('Return', float)]
            sorted_data = np.sort(
                np.array(transformed_data, dtype=dtype), order=method)
            return sorted_data
        return [["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]]
