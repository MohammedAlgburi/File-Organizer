from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtGui import QPixmap
from OptionsScreen import OptionsScreen
from Panel import Panel
from ModifyScreen import ModifyScreen
from AddPictureScreen import AddPictureScreen
from DisplayArea import DisplayArea

class FaceIdentificationScreen(QWidget):

    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()

        self.current_button: QPushButton
        self.current_image: QPixmap
        self.display_area = DisplayArea(self)
        self.modify_screen = ModifyScreen(self)
        self.panel = Panel(self)
        self.options_screen = OptionsScreen(self)
        self.add_picture_screen = AddPictureScreen(self)

        self.display_area.setCurrentWidget(self.options_screen)

        main_layout.addWidget(self.panel)
        main_layout.addWidget(self.display_area)        

        self.setLayout(main_layout)
    
    def load_setting_screen(self):
        SettingScreen()

class SettingScreen(QWidget):
    def __init__(self):
        super().__init__()

from PySide6.QtWidgets import QPushButton

class StateManager:
    def __init__(self, face_identification_screen) -> None:
        self.current_button: QPushButton
        self.face_identification_screen = face_identification_screen
        self.display_area = face_identification_screen.display_area

