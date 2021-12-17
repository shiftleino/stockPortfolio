from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


class StartWindow(QDialog):
    """Class that provides Start Window functionality.

    Inherits: QDialog
    """

    def __init__(self, main_widget):
        """Constructor for the Start Window class.

        Args:
            main_widget (QStackedWidget): The main widget that contains all the windows.
        """
        super().__init__()
        self.main_widget = main_widget
        self.layout = QVBoxLayout()
        self.set_labels()
        self.layout.addStretch(10)

        self.login_btn = self.create_login_btn()
        self.layout.addStretch(1)
        self.signup_btn = self.create_signup_btn()
        self.layout.addStretch(10)
        self.setLayout(self.layout)

        self.login_btn.clicked.connect(self.change_login)
        self.signup_btn.clicked.connect(self.change_signup)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")

    def set_labels(self):
        """Sets headers for the Start Window.
        """
        text = "Stock Portfolio Manager"
        subtext = "Welcome to the Stock Portfolio Manager."
        header = QLabel(text)
        subheader = QLabel(subtext)
        header.setStyleSheet(
            "color: #66FCF1; font-weight: bold; font-size: 80px")
        subheader.setStyleSheet(
            "color: white; font-weight: bold; font: Georgia; font-size: 40px")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        subheader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(header)
        self.layout.addWidget(subheader)

    def create_login_btn(self):
        """Creates a button for the user to login.
        """
        login_btn = QPushButton("Log in")
        login_layout = QHBoxLayout()
        login_layout.addStretch(1)
        login_btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        login_btn.setFixedSize(300, 50)
        login_layout.addWidget(login_btn)
        login_layout.addStretch(1)
        self.layout.addLayout(login_layout)
        return login_btn

    def create_signup_btn(self):
        """Creates a button for the user to sign up as a new user.
        """
        signup_btn = QPushButton("Sign up")
        signup_layout = QHBoxLayout()
        signup_layout.addStretch(1)
        signup_btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        signup_btn.setFixedSize(300, 50)
        signup_layout.addWidget(signup_btn)
        signup_layout.addStretch(1)
        self.layout.addLayout(signup_layout)
        return signup_btn

    def change_login(self):
        """Changes the window to the Login Window.
        """
        self.main_widget.setCurrentIndex(1)

    def change_signup(self):
        """Changes the window to the Sign Up Window
        """
        self.main_widget.setCurrentIndex(2)
