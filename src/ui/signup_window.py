from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class SignupWindow(QDialog):
    """Class for the window where the user can sign up as a new user.

    Args:
        QDialog: Inherits QDialog
    """
    def __init__(self, main_widget, repo):
        super().__init__()
        self.__user_repo = repo
        self.main_widget = main_widget
        self.layout = QVBoxLayout()
        self.set_labels()
        
        self.layout.addStretch(1)
        self.user_name_field, self.password_field = self.create_signup_form()
        self.error = self.error_label()
        self.signup_btn = self.create_signup_btn()
        self.layout.addStretch(1)
        self.login_btn = self.create_login_btn()
        self.layout.addStretch(10)
        self.setLayout(self.layout)

        self.signup_btn.clicked.connect(self.signup)
        self.login_btn.clicked.connect(self.change_to_login)

        # SET BACKGROUND FOR THE WINDOW
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")

    def set_labels(self):
        """Sets headers for the Log In Window.
        """
        text = "Stock Portfolio Manager"
        subtext = "Create a new account."
        header = QLabel(text)
        subheader = QLabel(subtext)

        header.setStyleSheet("color: #66FCF1; font-weight: bold; font-size: 80px")
        subheader.setStyleSheet("color: white; font-weight: bold; font: Georgia; font-size: 40px")

        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        subheader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(header)
        self.layout.addStretch(10)
        self.layout.addWidget(subheader)
    
    def create_signup_form(self):
        """Creates the form for signup.

        Returns:
            QLineEdit, QLineEdit: The textfields for username and password.
        """
        # USERNAME FIELD
        username_field = QLineEdit()
        username_field.setPlaceholderText("Enter username")
        username_field.setFixedSize(300, 50)
        username_field.setStyleSheet("background-color: white; color: black; font: Georgia; font-size: 18px")
        userform_layout = QHBoxLayout()
        userform_layout.addStretch()
        userform_layout.addWidget(username_field)
        userform_layout.addStretch()
        self.layout.addLayout(userform_layout)

        # PASSWORD FIELD
        password_field = QLineEdit()
        password_field.setPlaceholderText("Enter password")
        password_field.setFixedSize(300, 50)
        password_field.setStyleSheet("background-color: white; color: black; font: Georgia; font-size: 18px")
        password_field.setEchoMode(QLineEdit.EchoMode.Password)
        pwform_layout = QHBoxLayout()
        pwform_layout.addStretch()
        pwform_layout.addWidget(password_field)
        pwform_layout.addStretch()
        self.layout.addLayout(pwform_layout)
        return username_field, password_field

    def create_signup_btn(self):
        """Creates a button for the user to signup.

        Returns:
            QPushButton: The sign up button.
        """
        signup_btn = QPushButton("Sign up")
        signup_layout = QHBoxLayout()
        signup_layout.addStretch(1)
        signup_btn.setStyleSheet("QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        signup_btn.setFixedSize(300, 50)
        signup_layout.addWidget(signup_btn)
        signup_layout.addStretch(1)
        self.layout.addLayout(signup_layout)
        return signup_btn

    def create_login_btn(self):
        """Creates a button to login window if the user already has an account.

        Returns:
            QPushButton: The Login button.
        """
        login_btn = QPushButton("Already an account? Log in.")
        login_layout = QHBoxLayout()
        login_layout.addStretch(1)
        login_btn.setStyleSheet("QPushButton {background-color: #66FCF1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10} QPushButton::hover {background-color: #33C9C1; border-radius: 10px; font-weight: bold; font-size: 18px; color: #0B0C10}")
        login_btn.setFixedSize(300, 50)
        login_layout.addWidget(login_btn)
        login_layout.addStretch(1)
        self.layout.addLayout(login_layout)
        return login_btn

    def change_to_login(self):
        """Switches the window to the login window.
        """
        self.main_widget.setCurrentIndex(1)

    def error_label(self):
        """Creates the error text label for invalid username and/or password.

        Returns:
            QLabel: Error text.
        """
        label = QLabel("")
        label.setStyleSheet("color: red; font: Georgia; font-weight: bold; font-size: 18px")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(label)
        return label

    def signup(self):
        """Creates the user account and checks if successful.
        """
        username = self.user_name_field.text()
        password = self.password_field.text()
        if len(username) > 0 and len(password) > 0:
            successful = self.__user_repo.add_user(username, password)
            if successful:

                # SHOW THE Login WINDOW
                self.main_widget.setCurrentIndex(1)
            else:
                self.error.setText("Something went wrong. Try again with different username")
        else:
            self.error.setText("Please give valid username and password")
