import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from start_window import StartWindow

def start_gui():
    app = QApplication(sys.argv)
    start_window = StartWindow()
    main_widget = QStackedWidget()
    main_widget.addWidget(start_window)
    main_widget.setFixedHeight(800)
    main_widget.setFixedWidth(1200)
    main_widget.setWindowTitle("Stock Portfolio")

    sys.exit(app.exec_())
