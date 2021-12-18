from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from .portfolio_window import PortfolioWindow


class LoginWindow(QDialog):
    """Class for the window where the user can login in the application.

    Args:
        QDialog: Inherits QDialog
    """

    def __init__(self, main_widget, user_service, stock_service):
        """Constructor for the Login Window class.

        Args:
            main_widget (QStackedWidget): The main widget that contains all the windows.
            user_service (UserService): The UserService class for the application logic of the user.
            stock_service (StockService): The StockService class for the application logic of the portfolio.
        """
        super().__init__()
        self.__user_service = user_service
        self.__stock_service = stock_service
        self.main_widget = main_widget
        self.layout = QVBoxLayout()
        self.set_labels()
        self.layout.addStretch(1)
        self.user_name_field, self.password_field = self.create_login_form()
        self.error = self.error_label()
        self.login_btn = self.create_login_btn()
        self.layout.addStretch(1)
        self.no_account_btn = self.create_no_account_btn()
        self.layout.addStretch(10)
        self.setLayout(self.layout)

        self.login_btn.clicked.connect(self.login)
        self.no_account_btn.clicked.connect(self.change_to_signup)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")

    def set_labels(self):
        """Sets headers for the Log In Window.
        """
        text = "Stock Portfolio Manager"
        subtext = "Log in to your account."
        header = QLabel(text)
        subheader = QLabel(subtext)
        header.setStyleSheet(
            "color: #66FCF1; font-weight: bold; font-size: 80px")
        subheader.setStyleSheet(
            "color: white; font-weight: bold; font: Georgia; font-size: 40px")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        subheader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(header)
        self.layout.addStretch(10)
        self.layout.addWidget(subheader)

    def create_login_form(self):
        """Creates the form for login.

        Returns:
            QLineEdit, QLineEdit: The textfields for username and password.
        """
        username_field = QLineEdit()
        username_field.setPlaceholderText("Enter username")
        username_field.setFixedSize(300, 50)
        username_field.setStyleSheet(
            "background-color: white; color: black; font: Georgia; font-size: 18px")
        userform_layout = QHBoxLayout()
        userform_layout.addStretch()
        userform_layout.addWidget(username_field)
        userform_layout.addStretch()
        self.layout.addLayout(userform_layout)

        password_field = QLineEdit()
        password_field.setPlaceholderText("Enter password")
        password_field.setFixedSize(300, 50)
        password_field.setStyleSheet(
            "background-color: white; color: black; font: Georgia; font-size: 18px")
        password_field.setEchoMode(QLineEdit.EchoMode.Password)
        pwform_layout = QHBoxLayout()
        pwform_layout.addStretch()
        pwform_layout.addWidget(password_field)
        pwform_layout.addStretch()
        self.layout.addLayout(pwform_layout)
        return username_field, password_field

    def create_login_btn(self):
        """Creates a button for the user to login.

        Returns:
            QPushButton: The login button.
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

    def create_no_account_btn(self):
        """Creates a button to sign up window if the user does not have an account.

        Returns:
            QPushButton: The No Account button.
        """
        signup_btn = QPushButton("No account yet? Sign up.")
        signup_layout = QHBoxLayout()
        signup_layout.addStretch(1)
        signup_btn.setStyleSheet(
            "QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        signup_btn.setFixedSize(300, 50)
        signup_layout.addWidget(signup_btn)
        signup_layout.addStretch(1)
        self.layout.addLayout(signup_layout)
        return signup_btn

    def change_to_signup(self):
        """Switches the window to the sign up window.
        """
        self.user_name_field.clear()
        self.password_field.clear()
        self.main_widget.setCurrentIndex(2)

    def error_label(self):
        """Creates the error text label for invalid username and/or password.

        Returns:
            QLabel: Error text.
        """
        label = QLabel("")
        label.setStyleSheet(
            "color: red; font: Georgia; font-weight: bold; font-size: 18px")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(label)
        return label

    def login(self):
        """Checks if the user credentials are ok and then logs in.
        """
        username = self.user_name_field.text()
        password = self.password_field.text()
        if len(username) > 0 and len(password) > 0:
            successful = self.__user_service.login(username, password)
            if successful:
                self.user_name_field.clear()
                self.password_field.clear()

                new_id = self.__user_service.get_id(username)
                self.__stock_service.set_user_id(new_id)
                portfolio = PortfolioWindow(
                    self.main_widget, self.__user_service, self.__stock_service)
                self.main_widget.addWidget(portfolio)
                self.error.setText("")
                self.main_widget.setCurrentIndex(3)
            else:
                self.error.setText(
                    "Account does not exist or incorrect password")
        else:
            self.error.setText("Please give valid username and password")
