from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QSpacerItem
from PySide6.QtGui import QFont, Qt

class ModifyScreen(QWidget):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.display_area = self.state_manager.display_area
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.current = QPushButton()
        self.deletion_screen = ConfirmDeletionScreen(self.state_manager, self)
        self.display_area.addWidget(self.deletion_screen)

        self.top_header = QLabel()
        self.top_header.setFont(QFont("Ariel", 44))

        self.change_name_box = QTextEdit()
        self.change_name_box.setMaximumHeight(40)

        self.save_changes_button = QPushButton("Save Changes")
        self.save_changes_button.setMinimumWidth(200)

        self.delete_button = QPushButton("Delete?")
        self.delete_button.setMinimumWidth(200)

        self.screen_layout.addWidget(self.top_header, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.screen_layout.addSpacerItem(QSpacerItem(200, 60))
        self.screen_layout.addWidget(self.change_name_box, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.screen_layout.addStretch()

        self.screen_layout.addWidget(self.save_changes_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.screen_layout.addWidget(self.delete_button, alignment= Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.display_area.addWidget(self)

    def open(self):
        self.change_name_box.setText(self.state_manager.current_button.text())

        def save_changes():
            self.state_manager.current_button.setText(self.change_name_box.toPlainText())
            self.display_area.setCurrentWidget(self.display_area.image_label)

        self.save_changes_button.clicked.connect(lambda: save_changes())
    
        self.top_header.setText(self.state_manager.current_button.text())
        self.delete_button.clicked.connect(lambda: self.deletion_screen.open())

        self.display_area.setCurrentWidget(self)

class ConfirmDeletionScreen(QWidget):
    def __init__(self, state_manager, modify_screen):
        super().__init__()
        self.screen_layout = QVBoxLayout()
        self.setLayout(self.screen_layout)
        self.state_manager = state_manager
        self.display_area = self.state_manager.display_area
        self.modify_screen = modify_screen

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
        
    def open(self):
        self.confirmation_text.setText(f"Are you sure you want to delete {self.state_manager.current_button.text()}?")

        def delete_button_clicked():
            self.state_manager.current_button.deleteLater()
            self.display_area.setCurrentWidget(self.display_area.image_label)
        
        self.delete_button.clicked.connect(delete_button_clicked)
        self.back_button.clicked.connect(lambda: self.state_manager.set_display_widget(self.modify_screen))

        self.display_area.setCurrentWidget(self)