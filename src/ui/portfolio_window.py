import sys
sys.path.append("src/services")
from stock_service import StockService
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

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
        self.__stock_service = StockService(self.__user.return_id(), self.__user_repo.return_conn())
        self.main_widget = main_widget
        self.layout = QVBoxLayout()

        self.logout_btn = self.create_logout_btn()
        self.set_labels()
        self.layout.addStretch()

        self.add_btn = self.create_add_stock_btn()
        self.rm_btn = self.create_remove_stock_btn()
        self.rf_btn = self.create_refresh_btn()
        self.add_btns()
        
        self.setLayout(self.layout)

        # SET BACKGROUND FOR THE WINDOW
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")
    
    def set_labels(self):
        text = "Your stock portfolio"
        header = QLabel(text)
        header.setStyleSheet("color: #66FCF1; font-weight: bold; font-size: 64px")
        label_layout = QHBoxLayout()
        label_layout.addWidget(header)
        label_layout.addStretch()

        user_name = self.__user.return_username()
        text = f"You are logged in as user:\n{user_name}"
        user_header = QLabel(text)
        user_header.setStyleSheet("color: #66FCF1; font-weight: bold; font-size: 14px")
        
        logout_layout = QVBoxLayout()
        logout_layout.addWidget(self.logout_btn)
        logout_layout.addWidget(user_header)
        label_layout.addLayout(logout_layout)

        self.layout.addLayout(label_layout)

    def create_logout_btn(self):
        logout = QPushButton("Log out")
        logout.setStyleSheet("QPushButton {background-color: #CFC6C7; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        logout.setFixedSize(180, 50)
        return logout

    def create_table(self):
        pass
    
    def create_add_stock_btn(self):
        btn = QPushButton("Add stock")
        btn.setStyleSheet("QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def create_remove_stock_btn(self):
        btn = QPushButton("Remove stock")
        btn.setStyleSheet("QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def create_refresh_btn(self):
        btn = QPushButton("Refresh table")
        btn.setStyleSheet("QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        btn.setFixedSize(180, 50)
        return btn

    def add_btns(self):
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.rm_btn)
        btn_layout.addWidget(self.rf_btn)
        btn_layout.addStretch()
        self.layout.addLayout(btn_layout)

