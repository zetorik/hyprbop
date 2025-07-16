from PySide6.QtCore import QThread, QTimer, Qt, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from utils import get_cursor_pos, raw_move_window

class ShowThread(QThread):
    progress = Signal(int)
    finished = Signal()

    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

    def run(self):
        raw_move_window(self.x, self.y) 

        self.finished.emit()

class PopWindow(QWidget):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle(title)
        self.setFixedSize(2, 2)

        self.thread1 = ShowThread(*get_cursor_pos())

        
        self.thread1.finished.connect(lambda: self.setFixedSize(200, 50))

        QTimer.singleShot(0, lambda: self.thread1.start())

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.test = QPushButton()
        self.main_layout.addWidget(self.test)

