from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QPixmap, QDrag
import resources_rc as rc

class FaceIdentificationScreen(QWidget):
    def __init__(self):
        super().__init__()
        # THIS MIGHT BE A LOCAL VARIABLE BUT IM PUTTING IT HERE FOR NOW
        self.image_label = QLabel()

    def setup_ui(self):
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.picture_display())        

        self.setLayout(main_layout)

    def picture_display(self) -> QStackedWidget:
        # This widget controls the different states of this box.
        # This box has three states: 
        # 1. no-picture-selected, 
        # 2. drag and drop, 
        # 3. image (only one which consistently changes)
        
        picture_display_manager = QStackedWidget()

        no_picture_label = QLabel(pixmap=QPixmap(":/rc/Resources/Picture-Select-image.png"))
        # TODO: Make the resource for the drag and drop.
        # TODO: Create the drag and drop functionality
        drag_and_drop_label = QLabel(pixmap=QPixmap(""))

        picture_display_manager.addWidget(no_picture_label)
        picture_display_manager.addWidget(drag_and_drop_label)
        picture_display_manager.addWidget(self.image_label)

        picture_display_manager.setCurrentIndex(0)

        return picture_display_manager


    def refresh_image_label(self, image_path: str):
        self.image_label.clear()
        self.image_label.setPixmap(QPixmap(image_path))

    def people_panel(self):
        panel = QWidget()

    def create_name_label(self):
        pass