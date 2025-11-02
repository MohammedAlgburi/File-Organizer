from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtGui import QPixmap
from OptionsScreen import OptionsScreen
from Panel import Panel
from ModifyScreen import ModifyScreen
from AddPictureScreen import AddPictureScreen
from DisplayArea import DisplayArea
from FaceEmbeddingStorage import FaceEmbeddingStorage
from GallaryScreen import GallaryScreen

class FaceIdentificationScreen(QWidget):
    def __init__(self, face_embedding_storage: FaceEmbeddingStorage):
        super().__init__()
        main_layout = QHBoxLayout()
        self.face_embedding_storage = face_embedding_storage

        self.current_button: QPushButton
        self.current_image: QPixmap
        self.display_area: DisplayArea = DisplayArea(self)
        self.modify_screen: ModifyScreen = ModifyScreen(self)
        self.panel: Panel = Panel(self)
        self.options_screen: OptionsScreen = OptionsScreen(self)
        self.add_picture_screen: AddPictureScreen = AddPictureScreen(self)
        self.gallary_screen: GallaryScreen = GallaryScreen(self)

        # Startup Screen 
        # TODO Make this screen the gallary screen after that screen is done
        self.display_area.setCurrentWidget(self.gallary_screen.image_select_screen)

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

