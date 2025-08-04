import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QStackedWidget
from PySide6 import QtWidgets
from FaceIdentificationScreen import FaceIdentificationScreen

class App:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication([])
        
        self.main_window = MainWindow()
        self.main_window.show()

        style_sheet = self.load_style_sheet("Styles.qss")
        self.app.setStyleSheet(style_sheet)

        sys.exit(self.app.exec())
    
    def load_style_sheet(self, path):
        with open(path) as file:
            return file.read()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.resize(800, 600)
        self.page_manager = QStackedWidget()
        self.setCentralWidget(self.page_manager)

        self.face_identification_screen = FaceIdentificationScreen()

        self.page_manager.addWidget(self.face_identification_screen)
        self.page_manager.setCurrentWidget(self.face_identification_screen)

if __name__ == "__main__":
    pass