from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    """Class that provides Main Window functionality.

    Inherits: QMainWindow
    """

    def __init__(self):
        """
        """
        super().__init__()
        self.init_main_window()

    def init_main_window(self):
        """Initializes the Main Window
        """
        self.setGeometry(300, 100, 1200, 800)
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("Numeerisen datan visualisointikirjasto")