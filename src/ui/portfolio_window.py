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
        self.main_widget = main_widget
        self.layout = QVBoxLayout()

        self.logout_btn = self.create_logout()
        self.set_labels()
        self.layout.addStretch()

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

    def create_logout(self):
        logout = QPushButton("Log out")
        logout.setStyleSheet("QPushButton {background-color: #CFC6C7; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        logout.setFixedSize(180, 50)
        return logout

    def create_table(self):
        pass