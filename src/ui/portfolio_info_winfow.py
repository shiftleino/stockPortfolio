from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton


class PortfolioInfoWindow(QDialog):
    def __init__(self, main_widget, stock_service):
        super().__init__()
        self.__main_widget = main_widget
        self.__service = stock_service
        self.layout = QVBoxLayout()

        self.return_btn = QPushButton("Return to Portfolio")

        self.return_btn.clicked.connect(self.return_portfolio_window)

        self.layout.addWidget(self.return_btn)
        self.setLayout(self.layout)

    def return_portfolio_window(self):
        self.__main_widget.setCurrentIndex(3)
        self.__main_widget.removeWidget(self)