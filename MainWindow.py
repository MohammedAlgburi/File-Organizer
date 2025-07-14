import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QStackedWidget
from PySide6 import QtWidgets


def run_gui():
    app = QtWidgets.QApplication([])

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.resize(800, 600)
        self.page_manager = QStackedWidget()