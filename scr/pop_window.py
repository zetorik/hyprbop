from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

class PopWindow(QWidget):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle(title)
        self.setFixedSize(200, 50)

