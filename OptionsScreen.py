from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QFileDialog

class OptionsScreen(QWidget):
    def __init__(self, state_manager):
        super().__init__()
        self.BUTTON_FONT = QFont("Ariel", 32)
        self.state_manager = state_manager
        self.display_area = self.state_manager.display_area
        self.panel = self.state_manager.panel

        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.screen_layout.addStretch()

        self.image_path = QPushButton("Image Path")
        self.image_path.setFont(self.BUTTON_FONT)
        self.screen_layout.addWidget(self.image_path, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.screen_layout.addSpacerItem(QSpacerItem(100, 30))

        self.directory_button = QPushButton("Select Directory")
        self.directory_button.setFont(self.BUTTON_FONT)
        self.screen_layout.addWidget(self.directory_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.screen_layout.addStretch()

        self.display_area.addWidget(self)
        self.display_area.setCurrentWidget(self)

        def open_directory_dialog():
            dir = QFileDialog.getExistingDirectory(self, ("Select Directory"), options=QFileDialog.Option.ShowDirsOnly)
            dir.strip()
            if dir != "":
                self.panel.show()
            #TODO handle directory selection
        
        def add_pic_screen():
            self.display_area.setCurrentWidget(self.state_manager.add_picture_screen)
            self.panel.show()

        self.directory_button.clicked.connect(open_directory_dialog)
        self.image_path.clicked.connect(add_pic_screen)
