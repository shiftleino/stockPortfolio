from services.stock_service import StockService
from .stock_window import StockWindow
from .portfolio_info_winfow import PortfolioInfoWindow
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, QInputDialog, QMessageBox


class PortfolioWindow(QDialog):
    """Window for the Stock Portfolio of the logged in User.

    Args:
        QDialog (QDialog): Inherits class QDialog.
    """

    def __init__(self, main_widget, repo, user):
        """Constructor for the PortfolioWindow class.

        Args:
            main_widget (QStackedWidget): The main widget that contains all the windows.
            repo (UserRepository): The repository for the user.
            user (User): The user object.
        """
        super().__init__()
        self.__user = user
        self.__user_repo = repo
        self.__stock_service = StockService(
            self.__user.return_id(), self.__user_repo.return_conn())
        self.main_widget = main_widget
        self.layout = QVBoxLayout()

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")

        self.logout_btn = self.create_logout_btn()
        self.set_labels()
        self.layout.addStretch()

        self.table = self.set_table()
        self.populate_table()

        self.add_btn = self.create_btn("Add Stock", 185, 50)
        self.rm_btn = self.create_btn("Remove Stock", 185, 50)
        self.rf_btn = self.create_btn("Refresh Prices", 185, 50)
        self.info_btn = self.create_btn("View Graph of a Stock", 280, 50)
        self.portfolio_btn = self.create_btn("Portfolio Information", 280, 50)
        self.add_btns()

        self.setLayout(self.layout)

        self.add_btn.clicked.connect(self.add_stock)
        self.rf_btn.clicked.connect(self.refresh_prices)
        self.rm_btn.clicked.connect(self.remove_stock)
        self.logout_btn.clicked.connect(self.logout)
        self.info_btn.clicked.connect(self.stock_info)
        self.portfolio_btn.clicked.connect(self.portfolio_info)

    def set_labels(self):
        """Method for setting the labels for the window.
        """
        text = "Stock Portfolio"
        header = QLabel(text)
        header.setStyleSheet(
            "color: #66FCF1; font-weight: bold; font-size: 64px")
        label_layout = QHBoxLayout()
        label_layout.addWidget(header)
        label_layout.addStretch()

        user_name = self.__user.return_username()
        text = f"You are logged in as user:\n{user_name}"
        user_header = QLabel(text)
        user_header.setStyleSheet(
            "color: #66FCF1; font-weight: bold; font-size: 14px")

        logout_layout = QVBoxLayout()
        logout_layout.addWidget(self.logout_btn)
        logout_layout.addWidget(user_header)
        label_layout.addLayout(logout_layout)
        self.layout.addLayout(label_layout)

    def create_btn(self, text, x, y):
        """Method for adding a blue button on the window.

        Args:
            text (string): The text in the button.
            x (int): The width of the button.
            y (int): The height of the button.

        Returns:
            QPushButton: The created button.
        """
        btn = QPushButton(text)
        btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(x, y)
        return btn

    def create_logout_btn(self):
        """Creates a grey button for the log out functionality.

        Returns:
            QPushButton: The created button.
        """
        btn = QPushButton("Logout")
        btn.setStyleSheet(
            "QPushButton {background-color: #CFC6C7; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 59)
        return btn

    def set_table(self):
        """Sets up an empty table.

        Returns:
            QTableWidget: The created empty table.
        """
        table = QTableWidget()
        table.setMinimumWidth(1000)
        table.setMinimumHeight(600)
        table.setColumnCount(6)
        table.setFrameStyle(0)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        for i in range(0, 7):
            table.setColumnWidth(i, 190)
        self.set_table_headers(table)
        table.setShowGrid(False)
        self.layout.addWidget(table)
        return table

    def populate_table(self):
        """Populates the table of the window with data.
        """
        data = self.__stock_service.return_user_data()
        self.table.setRowCount(len(data))
        i = 0
        for stock in data:
            stockname_item = QTableWidgetItem(f"{stock[2]} ({stock[3]})")
            return_per = ((stock[6] - stock[5]) / stock[5]) * 100
            currentprice_item = QTableWidgetItem(f"{stock[6]:.2f}")
            returnper_item = QTableWidgetItem(f"{return_per:.2f} %")
            return_total = (stock[6] - stock[5])*stock[4]
            returntotal_item = QTableWidgetItem(f"{return_total:.2f} {stock[7]}")
            purchaseprice_item = QTableWidgetItem(str(stock[5]))
            amount_item = QTableWidgetItem(str(stock[4]))
            for j, item in enumerate([stockname_item, currentprice_item, purchaseprice_item, amount_item, returnper_item, returntotal_item]):
                item.setBackground(QColor("white"))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)
            i += 1

    def refresh_prices(self):
        """Refreshes the current prices.
        """
        tickers, _ = self.__stock_service.return_stock_tickers()
        data = self.__stock_service.return_user_data()
        for i, ticker in enumerate(tickers):
            price = self.__stock_service.get_stock_price(ticker)[0]
            stockname_item = QTableWidgetItem(f"{data[i][2]} ({data[i][3]})")
            return_per = ((price - data[i][5]) / data[i][5]) * 100
            currentprice_item = QTableWidgetItem(f"{price:.2f}")
            returnper_item = QTableWidgetItem(f"{return_per:.2f} %")
            return_total = (price - data[i][5])*data[i][4]
            returntotal_item = QTableWidgetItem(f"{return_total:.2f} {data[i][7]}")
            purchaseprice_item = QTableWidgetItem(str(data[i][5]))
            amount_item = QTableWidgetItem(str(data[i][4]))
            for j, item in enumerate([stockname_item, currentprice_item, purchaseprice_item, amount_item, returnper_item, returntotal_item]):
                item.setBackground(QColor("white"))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)

    def set_table_headers(self, table):
        """Sets the table headers.

        Args:
            table (QTableWidget): The table of the window.
        """
        labels = ["Stock", "Current price",
                  "Purchase price", "Amount", "Return-%", "Return"]
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        for i, label in enumerate(labels):
            item = QTableWidgetItem(label)
            item.setBackground(QColor("white"))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFont(font)
            table.setHorizontalHeaderItem(i, item)

    def add_btns(self):
        """Adds all the bottom buttons to the window.
        """
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.rm_btn)
        btn_layout.addWidget(self.rf_btn)
        btn_layout.addWidget(self.info_btn)
        btn_layout.addWidget(self.portfolio_btn)
        btn_layout.addStretch()
        self.layout.addLayout(btn_layout)

    def get_current_price(self, ticker):
        """Method for accessing the current price of the stock.

        Args:
            ticker (string): The ticker of the stock.

        Returns:
            float: The current price of the stock.
        """
        current = self.__stock_service.get_stock_price(ticker)
        return current

    def add_stock(self):
        """Adds a stock to the users portfolio if possible.
        """
        user_form = QInputDialog()
        user_form.setStyleSheet("font-size: 18px")
        name, ok1 = QInputDialog.getText(
            user_form, "Add new stock", "Enter the name of the stock:")
        if ok1 and len(name) != 0:
            ticker, ok2 = QInputDialog.getText(
                user_form, "Add new stock", "Enter the ticker of the stock:")
            if ok2 and len(ticker) != 0:
                amount, ok3 = QInputDialog.getInt(
                    user_form, "Add new stock", "Enter the amount:", min=0)
                if ok3:
                    buy_price, ok4 = QInputDialog.getDouble(
                        user_form, "Add new stock", "Enter the price you bought the stock:", min=0)
                    if ok4:
                        success = self.__stock_service.add_stock(
                            name, ticker, amount, buy_price)
                        self.populate_table()
                        if not success:
                            self.warning("StockError", "Something went wrong when adding the stock!\nCheck that you don't already have the stock in your portfolio\nand that the ticker format is the same as in Yahoo! Finance.")
                    else:
                        self.warning("InputError", "Check that you provide sensible input to all fields.")
                else:
                    self.warning("InputError", "Check that you provide sensible input to all fields.")
            else:
                self.warning("InputError", "Check that you provide sensible input to all fields.")
        else:
            self.warning("InputError", "Check that you provide sensible input to all fields.")

    def remove_stock(self):
        """Removes the stock from the user's portfolio if possible.
        """
        user_form = QInputDialog()
        user_form.setStyleSheet("font-size: 18px")
        ticker, ok = QInputDialog.getText(
            user_form, "Remove a stock", "Enter the ticker of the stock you want to remove:")
        if ok:
            success = self.__stock_service.remove_stock(ticker)
            if not success:
                self.warning("StockError", "Something went wrong when removing the stock!\nCheck that you have the stock in your portfolio.")
            else:
                self.populate_table()
        else:
            self.warning("InputError", "Check that you provide sensible input to all fields.")

    def warning(self, label, text):
        """Shows a warning message for the user.

        Args:
            label (string): The label of the warning.
            text (string): The explanation in the warning.
        """
        box = QMessageBox()
        box.setWindowTitle(label)
        box.setText(text)
        box.setIcon(QMessageBox.Critical)
        box.exec_()

    def logout(self):
        """Functionality for logging out.
        """
        self.__user.set_username(None)
        self.__user.set_id(None)
        self.__user.set_password(None)
        self.main_widget.setCurrentIndex(0)
        self.main_widget.removeWidget(self)

    def stock_info(self):
        """Functionality for changing to the stock graph window if possible.
        """
        form = QInputDialog()
        form.setStyleSheet("font-size: 18px")
        ticker, ok = QInputDialog.getText(
            form, "View graph of a stock", "Enter the ticker of the stock you want to view:")
        if ok:
            ok2 = self.__stock_service.check_if_ticker_in_db(ticker)
            if ok2:
                stock_window = StockWindow(
                    self.main_widget, self.__stock_service, ticker)
                self.main_widget.addWidget(stock_window)
                self.main_widget.setCurrentIndex(4)
            else:
                self.warning("StockError", "Something went wrong when trying to view the stock!\nCheck that you have the stock in your portfolio.")
        else:
            self.warning("InputError", "Check that you provide sensible input to all fields.")

    def portfolio_info(self):
        """Changes to the portfolio information window.
        """
        portfolio_info_window = PortfolioInfoWindow(self.main_widget, self.__stock_service)
        self.main_widget.addWidget(portfolio_info_window)
        self.main_widget.setCurrentIndex(4)