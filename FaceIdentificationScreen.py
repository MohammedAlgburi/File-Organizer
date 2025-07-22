from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QStackedWidget, QScrollArea, QPushButton
from PySide6.QtGui import QPixmap, QFont, Qt
from PySide6.QtCore import QMargins
import resources_rc as rc

class FaceIdentificationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.display_area = DisplayArea()

        self.modify_screen = ModifyScreen(self.display_area)
        self.panel = Panel(self.display_area, self.modify_screen)

    def setup_ui(self):
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.panel)
        main_layout.addWidget(self.display_area)        

        self.setLayout(main_layout)


class DisplayArea(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.no_picture_label = QLabel(pixmap=QPixmap(":/rc/Resources/Picture-Select-image.png"))
        # TODO: Make the resource for the drag and drop.
        # TODO: Create the drag and drop functionality
        self.drag_and_drop_label = QLabel(pixmap=QPixmap(""))
        self.image_label = QLabel()

        self.addWidget(self.no_picture_label)
        self.addWidget(self.drag_and_drop_label)
        self.addWidget(self.image_label)

        self.setCurrentIndex(0)

    def refresh_image_label(self, image_path: str):
        self.image_label.clear()
        self.image_label.setPixmap(QPixmap(image_path))

class ModifyScreen(QWidget):
    def __init__(self, display_area_instance: DisplayArea):
        super().__init__()
        self.display_area = display_area_instance
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.display_area.addWidget(self)

        self.top_header = QLabel()

        self.delete_button = QPushButton("Delete?")

        self.screen_layout.addWidget(self.top_header)
        self.screen_layout.addWidget(self.delete_button)
    
    def open_screen(self, button: QPushButton):

        def delete_button_clicked():
            button.deleteLater()
            self.display_area.setCurrentIndex(0)
    
        self.top_header.setText(button.text())
        self.delete_button.clicked.connect(delete_button_clicked)



class Panel(QScrollArea):
    def __init__(self, display_area_instance: DisplayArea, modify_screen_instance: ModifyScreen):
        super().__init__()
        self.panel_content = QWidget()
        self.panel_content_layout = QVBoxLayout()
        self.panel_content_layout.addStretch()
        self.panel_content_layout.addWidget(self.bottom_bar())
        self.display_area = display_area_instance
        self.modify_screen = modify_screen_instance
        self.setMaximumWidth(180)

        self.panel_content.setLayout(self.panel_content_layout)
        self.setWidgetResizable(True)
        self.setWidget(self.panel_content)

        self.add_name_button("JOHN")
        self.add_name_button("JOHN")
        self.add_name_button("JOHN")

    def bottom_bar(self) -> QWidget:
        bar = QWidget()
        bar_layout = QHBoxLayout()
        bar.setLayout(bar_layout)
        bar_layout.addStretch()

        setting_button = QPushButton("S")
        setting_button.setMaximumSize(20,20)
        setting_button.clicked.connect(lambda: self.display_area.setCurrentIndex(4))

        bar_layout.addWidget(setting_button, Qt.AlignmentFlag.AlignRight)

        return bar

    def add_name_button(self, name: str):
        button = NameButton(name, self.display_area, self.modify_screen)
        INSERT_INDEX = self.panel_content_layout.count() - 2

        self.panel_content_layout.insertWidget(INSERT_INDEX, button, alignment=Qt.AlignmentFlag.AlignTop)
# TODO TODO TODO: CREATE THE SETTING SCREE CLASS

class NameButton(QPushButton):
    def __init__(self, name: str, display_area_instance: DisplayArea, modify_screen_instance: ModifyScreen):
        super().__init__()
        self.modify_screen = modify_screen_instance
        self.display_area = display_area_instance
        
        self.name = name
        self.setFont(QFont("Ariel", 24))
        self.setText(self.name)

        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.display_area.setCurrentIndex(3)
        self.modify_screen.open_screen(self)