from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class LoginWindow(QWidget):
    """Class for the window where the user can login in the application.

    Args:
        QWidget ([type]): Inherits QWidget which is 
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.set_labels()

    def set_labels(self):
        text = "Stock Portfolio Manager"
        subtext = """Welcome to the Stock Portfolio manager.
        Please login to your account or click "Don't have an account yet?" if you
        don't have an account."""
        header = QLabel(text)
        subheader = QLabel(subtext)
        self.layout.addWidget(header)
        self.layout.addWidget(subheader)