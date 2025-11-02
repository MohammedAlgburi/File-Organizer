from PySide6.QtWidgets import QWidget, QStackedWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont, Qt


class GallaryScreen(QWidget):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.display_area = self.state_manager.display_area

        self.image_select_screen = ImageSelectScreen(self.state_manager)
        self.image_view = ImageView()

        self.display_area.addWidget(self.image_select_screen)
        self.display_area.addWidget(self.image_view)


# Contains all of the functionality
class ImageSelectScreen(QWidget):
    def __init__(self, state_manager):
        TITLE_FONT = QFont("Arial", 28)
        super().__init__()
        self.state_manager = state_manager
        self.display_area = state_manager.display_area
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.screen_layout.addStretch()
        self.setObjectName("NoBackgroundButton")

        self.title_message = QPushButton("Galary view")
        self.title_message.setFont(TITLE_FONT)

        self.select_image = QPushButton("Add Image")
        self.select_image.setFont(TITLE_FONT)
        self.select_image.clicked.connect(lambda: self.display_area.setCurrentWidget(self.state_manager.options_screen))


        self.screen_layout.addWidget(self.title_message, alignment=Qt.AlignmentFlag.AlignCenter)
        self.screen_layout.addWidget(self.select_image, alignment=Qt.AlignmentFlag.AlignCenter)
        self.screen_layout.addStretch()

class ImageView(QWidget):
    def __init__(self):
        super().__init__()
    
    def load_images(self):
        pass