import sys
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from FaceIdentificationScreen import FaceIdentificationScreen
from PySide6 import QtWidgets
from exceptions import CSSLoadError
from FaceEmbeddingStorage import FaceEmbeddingStorage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.resize(800, 600)
        self.page_manager = QStackedWidget()
        self.setCentralWidget(self.page_manager)

        self.face_embedding_storage = FaceEmbeddingStorage()
        self.face_identification_screen = FaceIdentificationScreen(self.face_embedding_storage)

        self.page_manager.addWidget(self.face_identification_screen)
        self.page_manager.setCurrentWidget(self.face_identification_screen)

class App:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication([])
        
        self.main_window = MainWindow()
        self.main_window.show()

        self.load_style_sheet(r"File-Organizer\Styles.qss")

        sys.exit(self.app.exec())
    
    def load_style_sheet(self, path):
        try:
            with open(path) as file:
                self.app.setStyleSheet(file.read())
        except:
            raise CSSLoadError()


image_path = "venv\\IMG_20250602_182834737.jpg"

if __name__ == "__main__":
    app = App()