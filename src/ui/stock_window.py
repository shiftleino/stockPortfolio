from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class StockWindow(QDialog):
    def __init__(self, main_widget, stock_service, ticker):
        super().__init__()
        self.__main_widget = main_widget
        self.__stock_service = stock_service
        self.__ticker = ticker

        self.layout = QVBoxLayout()

        # SET BACKGROUND FOR THE WINDOW
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")

        self.return_btn = self.create_btn("Return to portfolio")
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.return_btn)

        self.layout.addLayout(top_layout)

        self.return_btn.clicked.connect(self.return_portfolio_window)

        self.setLayout(self.layout)

    def create_btn(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def return_portfolio_window(self):
        self.__main_widget.setCurrentIndex(3)
        self.__main_widget.removeWidget(self)