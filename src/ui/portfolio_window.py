from services.stock_service import StockService
from .stock_window import StockWindow
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
        """
        super().__init__()
        self.__user = user
        self.__user_repo = repo
        self.__stock_service = StockService(
            self.__user.return_id(), self.__user_repo.return_conn())
        self.main_widget = main_widget
        self.layout = QVBoxLayout()

        # SET BACKGROUND FOR THE WINDOW
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

    def set_labels(self):
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
        btn = QPushButton(text)
        btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(x, y)
        return btn

    def create_logout_btn(self):
        btn = QPushButton("Logout")
        btn.setStyleSheet(
            "QPushButton {background-color: #CFC6C7; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 59)
        return btn

    def set_table(self):
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
        data = self.__stock_service.return_user_data()
        self.table.setRowCount(len(data))
        i = 0
        for stock in data:
            item = QTableWidgetItem(f"{stock[2]} ({stock[3]})")
            return_per = ((stock[6] - stock[5]) / stock[5]) * 100
            item2 = QTableWidgetItem(f"{stock[6]:.2f}")
            item5 = QTableWidgetItem(f"{return_per:.2f} %")
            return_total = (stock[6] - stock[5])*stock[4]
            item6 = QTableWidgetItem(f"{return_total:.2f} {stock[7]}")
            item3 = QTableWidgetItem(str(stock[5]))
            item4 = QTableWidgetItem(str(stock[4]))
            for j, item in enumerate([item, item2, item3, item4, item5, item6]):
                item.setBackground(QColor("white"))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)
            i += 1

    def refresh_prices(self):
        tickers, _ = self.__stock_service.return_stock_tickers()
        data = self.__stock_service.return_user_data()
        for i, ticker in enumerate(tickers):
            price = self.__stock_service.get_stock_price(ticker)[0]
            item = QTableWidgetItem(f"{data[i][2]} ({data[i][3]})")
            return_per = ((price - data[i][5]) / data[i][5]) * 100
            item2 = QTableWidgetItem(f"{price:.2f}")
            item5 = QTableWidgetItem(f"{return_per:.2f} %")
            return_total = (price - data[i][5])*data[i][4]
            item6 = QTableWidgetItem(f"{return_total:.2f} {data[i][7]}")
            item3 = QTableWidgetItem(str(data[i][5]))
            item4 = QTableWidgetItem(str(data[i][4]))
            for j, item in enumerate([item, item2, item3, item4, item5, item6]):
                item.setBackground(QColor("white"))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)

    def set_table_headers(self, table):
        labels = ["Stock", "Current price",
                  "Purchase price", "Amount", "Return-%", "Return"]
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        for i, label in enumerate(labels):
            item = QTableWidgetItem(label)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFont(font)
            table.setHorizontalHeaderItem(i, item)

    def add_btns(self):
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.rm_btn)
        btn_layout.addWidget(self.rf_btn)
        btn_layout.addWidget(self.info_btn)
        btn_layout.addWidget(self.portfolio_btn)
        btn_layout.addStretch()
        self.layout.addLayout(btn_layout)

    def get_current_price(self, ticker):
        current = self.__stock_service.get_stock_price(ticker)
        return current

    def add_stock(self):
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
                            self.warning_stock()
                    else:
                        self.warning_input()
                else:
                    self.warning_input()
            else:
                self.warning_input()
        else:
            self.warning_input()

    def remove_stock(self):
        user_form = QInputDialog()
        user_form.setStyleSheet("font-size: 18px")
        ticker, ok = QInputDialog.getText(
            user_form, "Remove a stock", "Enter the ticker of the stock you want to remove:")
        if ok:
            success = self.__stock_service.remove_stock(ticker)
            if not success:
                self.warning_remove()
            else:
                self.populate_table()
        else:
            self.warning_input()

    def warning_input(self):
        box = QMessageBox()
        box.setWindowTitle("InputError")
        box.setText(
            "Something went wrong!\nCheck that you provide sensible input to all fields.")
        box.setIcon(QMessageBox.Critical)
        box.exec_()

    def warning_stock(self):
        box = QMessageBox()
        box.setWindowTitle("StockError")
        box.setText(
            "Something went wrong when adding the stock!\nCheck that you don't already have the stock in your portfolio.")
        box.setIcon(QMessageBox.Critical)
        box.exec_()

    def warning_remove(self):
        box = QMessageBox()
        box.setWindowTitle("StockError")
        box.setText(
            "Something went wrong when removing the stock!\nCheck that you have the stock in your portfolio.")
        box.setIcon(QMessageBox.Critical)
        box.exec_()

    def warning_ticker(self):
        box = QMessageBox()
        box.setWindowTitle("StockError")
        box.setText(
            "Something went wrong when trying to view the stock!\nCheck that you have the stock in your portfolio.")
        box.setIcon(QMessageBox.Critical)
        box.exec_()

    def logout(self):
        self.__user.set_username(None)
        self.__user.set_id(None)
        self.__user.set_password(None)
        self.main_widget.setCurrentIndex(0)
        self.main_widget.removeWidget(self)

    def stock_info(self):
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
                self.warning_ticker()
        else:
            self.warning_input()
