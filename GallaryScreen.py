from PySide6.QtWidgets import QWidget, QStackedWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont

class GallaryScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.screen_manager = QStackedWidget(self)
        self.screen_manager.addWidget(_NoImagesScreen())
        self.screen_manager.addWidget(_PicturesScreen())

    
# Contains all of the functionality
class _NoImagesScreen(QWidget):
    def __init__(self):
        #TODO
        TITLE_FONT = QFont()
        super().__init__()
        self.screen_layout = QVBoxLayout()

        self.title_message = QLabel("Add Images To Gallary")
        self.title_message.setFont(TITLE_FONT)

        self.select_image = QPushButton("Add Image")

        self.select_dir = QPushButton("Add a Folder")

        self.screen_layout.addWidget(self.title_message)
        self.screen_layout.addWidget(self.select_image)
        self.screen_layout.addWidget(self.select_dir)


    

class _PicturesScreen(QWidget):
    def __init__(self):
        super().__init__()
    
    def load_images(self):
        pass