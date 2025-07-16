import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QStackedWidget
from PySide6 import QtWidgets
from FaceIdentificationScreen import FaceIdentificationScreen


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
        self.setCentralWidget(self.page_manager)

        self.setup_ui()
        
    def setup_ui(self):
        # THIS PART MIGHT GO GLOBAL IF I EVER NEED TO ACCESS IT LATER
        face_identification_screen = FaceIdentificationScreen()
        face_identification_screen.setup_ui()
        
        self.page_manager.addWidget(face_identification_screen)
        self.page_manager.setCurrentIndex(0)

if __name__ == "__main__":
    pass