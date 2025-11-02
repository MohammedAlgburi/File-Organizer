from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QSpacerItem
from PySide6.QtGui import QFont, Qt
from ImageAnalyzer import ImageAnalyzer, cv_image_to_qpixmap

class AddPictureScreen(QWidget):
    def __init__(self, state_manager):
        super().__init__()
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.state_manager = state_manager
        self.display_area = self.state_manager.display_area
        self.panel = self.state_manager.panel
        self.face_embedding_storage = self.state_manager.face_embedding_storage

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

        self.display_area.addWidget(self)
        self.display_area.setCurrentWidget(self)

    def add_image(self):
        image_path = self.image_path_text_box.toPlainText()

        image_analyzer = ImageAnalyzer()

        faces = image_analyzer.get_faces(image_path)
        faces_embeddings = [faces[i].embedding for i in range(len(faces))]
        self.face_embedding_storage.add_embeddings(faces_embeddings)
        image = image_analyzer.draw_box_around_face(image_path, faces[0].bbox)

        qpixmap = cv_image_to_qpixmap(image)

        scaled_pixmap = qpixmap.scaled(self.display_area.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.state_manager.current_image = scaled_pixmap
        self.display_area.set_image_label()
        self.panel.add_untitled_names(len(faces))

    def back_to_menu(self):
        self.display_area.setCurrentWidget(self.state_manager.options_screen)
        self.panel.hide()