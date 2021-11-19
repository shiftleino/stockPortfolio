import sys
sys.path.append("src/ui/")

from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtGui import QIcon
from start_window import StartWindow
from login_window import LoginWindow
from signup_window import SignupnWindow

def start_gui():
    app = QApplication(sys.argv)
    main_widget = QStackedWidget()
    start_window = StartWindow(main_widget)
    main_widget.addWidget(start_window)
    login_window = LoginWindow(main_widget)
    main_widget.addWidget(login_window)
    signup_window = SignupnWindow(main_widget)
    main_widget.addWidget(signup_window)
    main_widget.setFixedHeight(800)
    main_widget.setFixedWidth(1200)
    main_widget.setWindowTitle("Stock Portfolio")
    main_widget.setWindowIcon(QIcon("images/stock_icon.png"))
    main_widget.show()

    sys.exit(app.exec_())
