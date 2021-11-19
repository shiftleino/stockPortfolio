import sys
sys.path.append("src/ui/")

from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtGui import QIcon
from start_window import StartWindow
from login_window import LoginWindow
from signup_window import SignupWindow
from portfolio_window import PortfolioWindow
sys.path.clear()
sys.path.append("src")
from repositories.user_repository import UserRepository
from database import db_connection
from entities.user import User

def start_gui():
    app = QApplication(sys.argv)
    connection = db_connection.get_connection()
    user_repo = UserRepository(connection)
    user = User()
    main_widget = QStackedWidget()
    
    start_window = StartWindow(main_widget)
    main_widget.addWidget(start_window)

    login_window = LoginWindow(main_widget, user_repo, user)
    main_widget.addWidget(login_window)

    signup_window = SignupWindow(main_widget)
    main_widget.addWidget(signup_window)

    # WINDOW SETTINGS
    main_widget.setFixedHeight(800)
    main_widget.setFixedWidth(1200)
    main_widget.setWindowTitle("Stock Portfolio")
    main_widget.setWindowIcon(QIcon("images/stock_icon.png"))
    main_widget.show()

    sys.exit(app.exec_())
