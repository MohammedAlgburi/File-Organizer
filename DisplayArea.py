from PySide6.QtWidgets import QStackedWidget, QLabel
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtCore import Qt

class DisplayArea(QStackedWidget):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.setObjectName("DisplayArea")
        self.drag_and_drop_label = QLabel(pixmap=QPixmap(""))

        self.image_label = ImageLabel(QPixmap())

        self.addWidget(self.drag_and_drop_label)
        self.addWidget(self.image_label)

    def set_image_label(self):
        self.image_label.clear()
        self.image_label.setPixmap(self.state_manager.current_image)
        self.setCurrentWidget(self.image_label)

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