from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import Qt, QFont

class Panel(QScrollArea):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.modify_screen = self.state_manager.modify_screen
        self.display_area = self.state_manager.display_area
        self.setObjectName("Panel")
        self.panel_content = QWidget()
        self.panel_content.setObjectName("PanelContent")
        self.panel_content_layout = QVBoxLayout()

        self.add_image_button = Button("+")
        self.add_image_button.setFont(QFont("Arial", 18))
        self.add_image_button.clicked.connect(lambda: (self.display_area.setCurrentWidget(self.state_manager.options_screen), self.hide(), None)[-1])
        self.panel_content_layout.addWidget(self.add_image_button)

        self.setting_button = QPushButton("S")
        self.setting_button.setMaximumSize(20,20)

        self.panel_content_layout.addStretch()
        self.panel_content_layout.addWidget(self._bottom_bar())
        self.setMaximumWidth(180)

        self.panel_content.setLayout(self.panel_content_layout)
        self.setWidgetResizable(True)
        self.setWidget(self.panel_content)

        self.hide()

    def _bottom_bar(self) -> QWidget:
        bar = QWidget()
        bar_layout = QHBoxLayout()
        bar.setLayout(bar_layout)
        bar_layout.addStretch()

        help_button = QPushButton("H")
        help_button.setMinimumSize(20,20)

        bar_layout.addWidget(help_button, alignment=Qt.AlignmentFlag.AlignRight)
        bar_layout.addWidget(self.setting_button, Qt.AlignmentFlag.AlignRight)

        return bar

    def add_name_button(self, name= "Unnamed") -> QPushButton:
        button = Button(name)
        
        def clicked():
            self.state_manager.current_button = button
            self.modify_screen.open()


        button.clicked.connect(clicked)
        
        INSERT_INDEX = self.panel_content_layout.count() - 2
        self.panel_content_layout.insertWidget(INSERT_INDEX, button, alignment=Qt.AlignmentFlag.AlignTop)

        return button


    def add_untitled_names(self, amount):
        for _ in range(amount):
            self.add_name_button()

class Button(QPushButton):
    def __init__(self, name: str):
        super().__init__()
        self.setText(name)
        self.setProperty("type", "Standard_Button")
        self.setMinimumHeight(30)