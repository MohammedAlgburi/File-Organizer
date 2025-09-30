from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QStackedWidget, QScrollArea, QPushButton, QTextEdit, QSpacerItem, QFileDialog, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QFont, QResizeEvent, Qt
from ImageAnalyzer import ImageAnalyzer, cv_image_to_qpixmap

class FaceIdentificationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.display_area = DisplayArea()

        self.modify_screen = ModifyScreen(self)
        self.panel = Panel(self)
        self.confirm_deletion_screen = ConfirmDeletionScreen(self)
        self.setting_screen = SettingScreen()
        self.add_picture_screen = AddPictureScreen(self)
        self.options_screen = OptionsScreen(self)

        self.panel.hide()

        self.display_area.setCurrentWidget(self.options_screen)

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.panel)
        main_layout.addWidget(self.display_area)        

        self.setLayout(main_layout)


class DisplayArea(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("DisplayArea")
        self.drag_and_drop_label = QLabel(pixmap=QPixmap(""))

        self.image_label = ImageLabel(QPixmap())

        self.addWidget(self.drag_and_drop_label)
        self.addWidget(self.image_label)

    def set_image_label(self, image: QPixmap):
        self.image_label.clear()
        self.image_label.setPixmap(image)
        self.setCurrentWidget(self.image_label)

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
            self.face_id.display_area.setCurrentWidget(self.face_id.add_picture_screen)
        
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
        self.current_button = QPushButton()

        self.top_header = QLabel()
        self.top_header.setFont(QFont("Ariel", 44))

        self.change_name_box = QTextEdit()
        self.change_name_box.setMaximumHeight(40)

        self.save_changes_button = QPushButton("Save Changes")
        self.save_changes_button.clicked.connect(self.save_changes)
        self.save_changes_button.setMinimumWidth(200)

        self.delete_button = QPushButton("Delete?")
        self.delete_button.setMinimumWidth(200)

        self.screen_layout.addWidget(self.top_header, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.screen_layout.addSpacerItem(QSpacerItem(200, 60))
        self.screen_layout.addWidget(self.change_name_box, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.screen_layout.addStretch()

        self.screen_layout.addWidget(self.save_changes_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.screen_layout.addWidget(self.delete_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

    def open(self, button: QPushButton):
        self.current_button = button
        self.change_name_box.setText(button.text())
    
        self.top_header.setText(button.text())
        self.delete_button.clicked.connect(lambda: self.face_id.confirm_deletion_screen.open(self.current_button))

        self.face_id.display_area.setCurrentWidget(self)

    def save_changes(self):
        pass

class Panel(QScrollArea):
    def __init__(self, face_id: FaceIdentificationScreen):
        super().__init__()
        self.setObjectName("Panel")
        self.panel_content = QWidget()
        self.panel_content.setObjectName("PanelContent")
        self.panel_content_layout = QVBoxLayout()
        self.panel_content_layout.addStretch()
        self.panel_content_layout.addWidget(self.bottom_bar())
        self.face_id = face_id
        self.setMaximumWidth(180)

        self.panel_content.setLayout(self.panel_content_layout)
        self.setWidgetResizable(True)
        self.setWidget(self.panel_content)

    def add_untitled_names(self, amount):
        for _ in range(amount):
            self.add_name_button()


    def bottom_bar(self) -> QWidget:
        bar = QWidget()
        bar_layout = QHBoxLayout()
        bar.setLayout(bar_layout)
        bar_layout.addStretch()

        setting_button = QPushButton("S")
        setting_button.setMaximumSize(20,20)
        setting_button.clicked.connect(lambda: self.face_id.display_area.setCurrentWidget(self.face_id.setting_screen))

        help_button = QPushButton("H")
        help_button.setMinimumSize(20,20)

        bar_layout.addWidget(help_button, alignment=Qt.AlignmentFlag.AlignRight)
        bar_layout.addWidget(setting_button, Qt.AlignmentFlag.AlignRight)

        return bar

    def add_name_button(self, name= "Unnamed"):
        button = QPushButton(name)
        button.clicked.connect(lambda: self.face_id.modify_screen.open(button))
        button.setProperty("type", "Standard_Button")
        button.setMinimumHeight(30)
        
        INSERT_INDEX = self.panel_content_layout.count() - 2
        self.panel_content_layout.insertWidget(INSERT_INDEX, button, alignment=Qt.AlignmentFlag.AlignTop)

class AddPictureScreen(QWidget):
    def __init__(self, face_id_screen: FaceIdentificationScreen):
        super().__init__()
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.face_id = face_id_screen

        self.main_header = QLabel("Image Path")
        self.main_header.setFont(QFont("Ariel", 44))

        self.image_path_text_box = QTextEdit()
        self.image_path_text_box.setMaximumHeight(150)

        self.back_to_menu_button = QPushButton("Back to Menu")
        self.back_to_menu_button.clicked.connect(self.back_to_menu)
        self.back_to_menu_button.setMinimumWidth(200)

        self.add_image_button = QPushButton("Add Picture")
        self.add_image_button.setMinimumWidth(90)
        self.add_image_button.clicked.connect(self.add_image)
        self.add_image_button.setProperty("type", "Standard_Button")

        self.screen_layout.addWidget(self.main_header, alignment= Qt.AlignmentFlag.AlignHCenter)
        self.screen_layout.addSpacerItem(QSpacerItem(20, 10))
        self.screen_layout.addWidget(self.image_path_text_box, alignment= Qt.AlignmentFlag.AlignHCenter)
        self.screen_layout.addSpacerItem(QSpacerItem(20, 10))
        self.screen_layout.addWidget(self.add_image_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.screen_layout.addStretch()
        self.screen_layout.addWidget(self.back_to_menu_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.face_id.display_area.addWidget(self)
        self.face_id.display_area.setCurrentWidget(self)

    def add_image(self):
        image_path = self.image_path_text_box.toPlainText()

        image_analyzer = ImageAnalyzer()

        faces = image_analyzer.get_faces(image_path)
        image = image_analyzer.draw_box_around_face(image_path, faces[0].bbox)

        qpixmap = cv_image_to_qpixmap(image)

        scaled_pixmap = qpixmap.scaled(self.face_id.display_area.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.face_id.display_area.set_image_label(scaled_pixmap)

    def back_to_menu(self):
        self.face_id.display_area.setCurrentWidget(self.face_id.options_screen)
        self.face_id.panel.hide()

class OptionsScreen(QWidget):
    def __init__(self, face_id_screen: FaceIdentificationScreen):
        super().__init__()
        self.face_id = face_id_screen
        self.face_id.display_area.addWidget(self)

        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)

        self.image_path = QPushButton("Image Path")
        self.image_path.setFont(QFont("Ariel", 32))
        self.screen_layout.addWidget(self.image_path, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.image_path.clicked.connect(self.add_picture_screen)

        self.directory_button = QPushButton("Select Directory")
        self.directory_button.setFont(QFont("Ariel", 32))
        self.screen_layout.addWidget(self.directory_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.directory_button.clicked.connect(self.open_directory_dialog)
        
    def open_directory_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.exec()

        self.face_id.panel.show()
    def add_picture_screen(self):
        self.face_id.display_area.setCurrentWidget(self.face_id.add_picture_screen)
        self.face_id.panel.show()

class ImageLabel(QLabel):
    def __init__(self, pixmap: QPixmap):
        super().__init__()
        self._pixmap = QPixmap(pixmap)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not self._pixmap.isNull():
            label_size = self.size()

            scaled_pixmap = self._pixmap.scaled(label_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            self.setPixmap(scaled_pixmap)

        super().resizeEvent(event)