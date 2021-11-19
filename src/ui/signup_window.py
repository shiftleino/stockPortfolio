from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class SignupnWindow(QDialog):
    """Class for the window where the user can sign up as a new user.

    Args:
        QDialog: Inherits QDialog
    """
    def __init__(self, main_widget):
        super().__init__()
        self.main_widget = main_widget
        self.layout = QVBoxLayout()
        self.set_labels()
        
        self.setLayout(self.layout)

    def set_labels(self):
        """Sets headers for the Log In Window.
        """
        text = "Stock Portfolio Manager"
        subtext = "Welcome to the Stock Portfolio Manager."
        header = QLabel(text)
        subheader = QLabel(subtext)

        header.setStyleSheet("color: #66FCF1; font-weight: bold; font-size: 80px")
        subheader.setStyleSheet("color: white; font-weight: bold; font: Georgia; font-size: 40px")

        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        subheader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(header)
        self.layout.addWidget(subheader)

    