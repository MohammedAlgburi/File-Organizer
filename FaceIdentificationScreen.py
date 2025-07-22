from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QStackedWidget, QScrollArea, QPushButton, QTextEdit
from PySide6.QtGui import QPixmap, QFont, Qt
from PySide6.QtCore import QMargins
import resources_rc as rc

class FaceIdentificationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.display_area = DisplayArea()

        self.confirm_deletion_screen = ConfirmDeletionScreen()
        self.modify_screen = ModifyScreen(self.display_area, self.confirm_deletion_screen)
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
# TODO TODO TODO: CREATE THE SETTING SCREE CLASS

class ConfirmDeletionScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)

        self.confirmation_text = QLabel("Are You Sure You Want to Delete Name?")
        self.confirmation_text.setFont(QFont("Ariel", 24))

        self.delete_button = QPushButton("DELETE")

        self.screen_layout.addWidget(self.confirmation_text)
        self.screen_layout.addWidget(self.delete_button)

    def open(self, button: QPushButton, display_area: DisplayArea):
        display_area.addWidget(self)
        display_area.setCurrentWidget(self)

        def delete_button_clicked():
            button.deleteLater()
            display_area.setCurrentIndex(0)
        
        self.delete_button.clicked.connect(delete_button_clicked)

class ModifyScreen(QWidget):
    def __init__(self, display_area_instance: DisplayArea, confirm_deletion_screen_instance: ConfirmDeletionScreen):
        super().__init__()
        self.display_area = display_area_instance
        self.confirm_deletion_screen = confirm_deletion_screen_instance
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.display_area.addWidget(self)

        self.top_header = QLabel()
        self.top_header.setFont(QFont("Ariel", 34))

        self.change_name_box = QTextEdit()

        self.save_changes_button = QPushButton("Save Changes")
        self.save_changes_button.clicked.connect(self.save_changes)

        self.delete_button = QPushButton("Delete?")
        self.delete_button.setMinimumWidth(200)

        self.screen_layout.addWidget(self.top_header, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.screen_layout.addWidget(self.change_name_box, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.screen_layout.addStretch()

        self.screen_layout.addWidget(self.save_changes_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.screen_layout.addWidget(self.delete_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
    
    def open_screen(self, button: QPushButton):

        def delete_confirmation_screen():
            self.confirm_deletion_screen.open(button, self.display_area)

        self.change_name_box.setText(button.text())
    
        self.top_header.setText(button.text())
        self.delete_button.clicked.connect(delete_confirmation_screen)

    def save_changes(self):
        pass

class NameButton(QPushButton):
    def __init__(self, name: str, display_area_instance: DisplayArea, modify_screen_instance: ModifyScreen):
        super().__init__()
        self.modify_screen = modify_screen_instance
        self.display_area = display_area_instance
        
        self.name = name
        self.setText(self.name)

        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.display_area.setCurrentIndex(3)
        self.modify_screen.open_screen(self)

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