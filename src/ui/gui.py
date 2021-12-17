from .signup_window import SignupWindow
from .login_window import LoginWindow
from .start_window import StartWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys


def start_gui(user_repo, user):
    """Function for starting the GUI.

    Args:
        user_repo (UserRepository): The database functionality for the user.
        user (User): The user class.
    """
    app = QApplication(sys.argv)
    main_widget = QStackedWidget()

    start_window = StartWindow(main_widget)
    main_widget.addWidget(start_window)

    login_window = LoginWindow(main_widget, user_repo, user)
    main_widget.addWidget(login_window)

    signup_window = SignupWindow(main_widget, user_repo)
    main_widget.addWidget(signup_window)

    main_widget.setFixedHeight(800)
    main_widget.setFixedWidth(1200)
    main_widget.setWindowTitle("Stock Portfolio")
    main_widget.setWindowIcon(QIcon("images/stock_icon.png"))
    main_widget.show()

    sys.exit(app.exec_())
