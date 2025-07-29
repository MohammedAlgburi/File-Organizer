from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QStackedWidget, QScrollArea, QPushButton, QTextEdit, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap, QFont, Qt
from PySide6.QtCore import QMargins
import resources_rc as rc

class FaceIdentificationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.display_area = DisplayArea()
        self.setStyleSheet("background-color: green")

        self.modify_screen = ModifyScreen(self)
        self.panel = Panel(self)
        self.confirm_deletion_screen = ConfirmDeletionScreen(self)
        self.setting_screen = SettingScreen()

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.panel)
        main_layout.addWidget(self.display_area)        

        self.setLayout(main_layout)


class DisplayArea(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.no_picture_label = QLabel(pixmap=QPixmap(":/rc/Resources/Picture-Select-image.png"))
        self.no_picture_label.setStyleSheet("background-color: blue")
        self.no_picture_label.setScaledContents(True)
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

class SettingScreen(QWidget):
    def __init__(self):
        super().__init__()

class ConfirmDeletionScreen(QWidget):
    def __init__(self, face_id: FaceIdentificationScreen):
        super().__init__()
        self.face_id = face_id
        self.face_id.display_area.addWidget(self)
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)

        self.confirmation_text = QLabel()
        self.confirmation_text.setFont(QFont("Ariel", 24))

        self.delete_button = QPushButton("DELETE")
        self.delete_button.setMinimumWidth(200)

        self.back_button = QPushButton("Go Back")
        self.back_button.setMinimumWidth(200)

        self.screen_layout.addSpacerItem(QSpacerItem(200, 250))
        self.screen_layout.addWidget(self.confirmation_text, alignment= Qt.AlignmentFlag.AlignCenter)
        self.screen_layout.addStretch()
        self.screen_layout.addWidget(self.back_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.screen_layout.addWidget(self.delete_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

    def open(self, button: QPushButton):
        self.confirmation_text.setText(f"Are you sure you want to delete {button.text()}?")

        def delete_button_clicked():
            button.deleteLater()
            self.face_id.display_area.setCurrentWidget(self.face_id.display_area.no_picture_label)
        
        self.delete_button.clicked.connect(delete_button_clicked)
        self.back_button.clicked.connect(lambda: self.face_id.display_area.setCurrentWidget(self.face_id.modify_screen))

        self.face_id.display_area.setCurrentWidget(self)

class ModifyScreen(QWidget):
    def __init__(self, face_id: FaceIdentificationScreen,):
        super().__init__()
        self.face_id = face_id
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.face_id.display_area.addWidget(self)

        self.top_header = QLabel()
        self.top_header.setFont(QFont("Ariel", 34))

        self.change_name_box = QTextEdit()

        self.save_changes_button = QPushButton("Save Changes")
        self.save_changes_button.clicked.connect(self.save_changes)
        self.save_changes_button.setMinimumWidth(200)

        self.delete_button = QPushButton("Delete?")
        self.delete_button.setMinimumWidth(200)

        self.screen_layout.addWidget(self.top_header, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.screen_layout.addWidget(self.change_name_box, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.screen_layout.addStretch()

        self.screen_layout.addWidget(self.save_changes_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.screen_layout.addWidget(self.delete_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
    
    def open(self, button: QPushButton):
        self.change_name_box.setText(button.text())
    
        self.top_header.setText(button.text())
        self.delete_button.clicked.connect(lambda: self.face_id.confirm_deletion_screen.open(button))

        self.face_id.display_area.setCurrentWidget(self)

    def save_changes(self):
        pass

class NameButton(QPushButton):
    def __init__(self, name: str):
        super().__init__()
        
        self.name = name
        self.setText(self.name)

class Panel(QScrollArea):
    def __init__(self, face_id: FaceIdentificationScreen):
        super().__init__()
        self.panel_content = QWidget()
        self.panel_content_layout = QVBoxLayout()
        self.panel_content_layout.addStretch()
        self.panel_content_layout.addWidget(self.bottom_bar())
        self.face_id = face_id
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
        setting_button.clicked.connect(lambda: self.face_id.display_area.setCurrentWidget(self.face_id.setting_screen))

        bar_layout.addWidget(setting_button, Qt.AlignmentFlag.AlignRight)

        return bar

    def add_name_button(self, name: str):
        button = NameButton(name)
        button.clicked.connect(lambda: self.face_id.modify_screen.open(button))
        
        INSERT_INDEX = self.panel_content_layout.count() - 2
        self.panel_content_layout.insertWidget(INSERT_INDEX, button, alignment=Qt.AlignmentFlag.AlignTop)