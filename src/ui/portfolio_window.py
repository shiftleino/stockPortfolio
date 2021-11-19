from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel
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

        self.__username=self.__user.return_username()
        label = QLabel(f"Stock Portfolio {self.__username}")
        self.layout.addWidget(label)
        self.setLayout(self.layout)

        # SET BACKGROUND FOR THE WINDOW
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #1F2833")