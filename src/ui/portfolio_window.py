from services.stock_service import StockService
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

        self.logout_btn = self.create_logout_btn()
        self.set_labels()
        self.layout.addStretch()

        self.table = self.set_table()
        self.populate_table()

        self.add_btn = self.create_add_stock_btn()
        self.rm_btn = self.create_remove_stock_btn()
        self.rf_btn = self.create_refresh_btn()
        self.add_btns()

        self.setLayout(self.layout)

        self.add_btn.clicked.connect(self.add_stock)
        self.rf_btn.clicked.connect(self.populate_table)
        self.rm_btn.clicked.connect(self.remove_stock)
        self.logout_btn.clicked.connect(self.logout)

        # SET BACKGROUND FOR THE WINDOW
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")

    def set_labels(self):
        text = "Your stock portfolio"
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

    def create_logout_btn(self):
        logout = QPushButton("Log out")
        logout.setStyleSheet(
            "QPushButton {background-color: #CFC6C7; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        logout.setFixedSize(180, 50)
        return logout

    def set_table(self):
        table = QTableWidget()
        table.setMinimumWidth(1000)
        table.setMinimumHeight(600)
        table.setColumnCount(5)
        table.setFrameStyle(0)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        for i in range(0, 6):
            table.setColumnWidth(i, 200)
        table.horizontalHeader().setStyleSheet(
            "background-color: #1F2833; color: #1F2833")
        self.set_table_headers(table)
        table.setShowGrid(False)
        self.layout.addWidget(table)
        return table

    def populate_table(self):
        data = self.__stock_service.return_user_data()
        self.table.setRowCount(len(data))
        i = 0
        for stock in data:
            item = QTableWidgetItem(stock[2])
            current = self.get_current_price(stock[3])
            return_per = ((current - stock[5]) / stock[5]) * 100
            item2 = QTableWidgetItem(str(current))
            item3 = QTableWidgetItem(str(stock[5]))
            item4 = QTableWidgetItem(str(stock[4]))
            item5 = QTableWidgetItem(str(return_per) + " %")
            for j, item in enumerate([item, item2, item3, item4, item5]):
                item.setBackground(QColor("white"))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)
            i += 1

    def set_table_headers(self, table):
        labels = ["Stock", "Current price",
                  "Purchase price", "Amount", "Return-%"]
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        for i, label in enumerate(labels):
            item = QTableWidgetItem(label)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFont(font)
            table.setHorizontalHeaderItem(i, item)

    def create_add_stock_btn(self):
        btn = QPushButton("Add stock")
        btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def create_remove_stock_btn(self):
        btn = QPushButton("Remove stock")
        btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def create_refresh_btn(self):
        btn = QPushButton("Refresh table")
        btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def add_btns(self):
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.rm_btn)
        btn_layout.addWidget(self.rf_btn)
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

    def logout(self):
        self.__user.set_username(None)
        self.__user.set_id(None)
        self.__user.set_password(None)
        self.main_widget.setCurrentIndex(0)
        self.main_widget.removeWidget(self)
