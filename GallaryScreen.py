from PySide6.QtWidgets import QWidget, QStackedWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QFont, Qt


class GallaryScreen(QWidget):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.display_area = self.state_manager.display_area

        self.gallary_view = GallaryView(self.state_manager)

        self.image_select_screen = ImageSelectScreen(self.state_manager)
        self.image_select_screen.gallary_view_button.clicked.connect(lambda: self.display_area.setCurrentWidget(self.gallary_view))
        
        self.gallary_view.back_button.clicked.connect(lambda: self.display_area.setCurrentWidget(self.image_select_screen))

        self.display_area.addWidget(self.image_select_screen)
        self.display_area.addWidget(self.gallary_view)

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

        self.gallary_view_button = QPushButton("Galary view")
        self.gallary_view_button.setFont(TITLE_FONT)

        self.select_image = QPushButton("Add Image")
        self.select_image.setFont(TITLE_FONT)
        self.select_image.clicked.connect(lambda: self.display_area.setCurrentWidget(self.state_manager.options_screen))


        self.screen_layout.addWidget(self.gallary_view_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.screen_layout.addWidget(self.select_image, alignment=Qt.AlignmentFlag.AlignCenter)
        self.screen_layout.addStretch()

class GallaryView(QWidget):

    def __init__(self, state_manager):
        super().__init__()
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.state_manager = state_manager

        self.top_bar = QWidget()
        self.top_bar.setObjectName("TopBar")
        self.display_area = self.state_manager.display_area
        self.bar_layout = QHBoxLayout()
        self.top_bar.setLayout(self.bar_layout)

        self.back_button = QPushButton("⇐")
        self.back_button.setFont(QFont("Ariel", 16))
        self.back_button.setMinimumWidth(40)

        self.gallary_view_label = QLabel("Gallary View")
        self.gallary_view_label.setFont(QFont("Ariel", 14))

        self.bar_layout.addWidget(self.back_button)
        self.bar_layout.addStretch()
        self.bar_layout.addWidget(self.gallary_view_label)

        self.screen_layout.addWidget(self.top_bar)
        self.screen_layout.addStretch()

    def load_images(self):
        pass