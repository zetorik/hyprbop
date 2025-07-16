from PySide6.QtCore import QThread, QTimer, Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from pop_window import PopWindow
from get_config import Config
from utils import get_cursor_pos, raw_move_window, set_window_prop
from time import sleep

class ShowThread(QThread):
    progress = Signal(int)
    finished = Signal()

    def __init__(self, x: int, y: int, animation_enabled: bool):
        super().__init__()
        self.x = x
        self.y = y
        self.animation_enabled = animation_enabled

    def run(self):
        raw_move_window(self.x, self.y, self.animation_enabled) 

        self.finished.emit()

class PopHolder(QWidget):
    def __init__(self, config: Config) -> None:
        super().__init__()

        self.config = config
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle(config.title)
        self.setFixedSize(2, 2)
        self.setContentsMargins(0, 0, 0, 0)

        self.pop_window = PopWindow(config)
        self.pop_window.closing.connect(self.close)
        self.pop_window.setParent(self)
    
        cursor_pos = get_cursor_pos()
        new_pos = [cursor_pos[0] + config.x_offset, cursor_pos[1] + config.y_offset]

        if config.static_x:
            new_pos[0] = config.static_x
        if config.static_y:
            new_pos[1] = config.static_y

        self.thread1 = ShowThread(new_pos[0], new_pos[1], config.animation_enabled)
        self.thread1.finished.connect(self.on_show)

        QTimer.singleShot(0, lambda: self.thread1.start())

    def on_show(self) -> None:
        self.show_pop()

        self.setFixedSize(self.config.width, self.config.height)
              
        if self.config.no_system_border:
            set_window_prop("noborder", "on")

    def show_pop(self) -> None:
        self.pop_window.setFixedSize(self.config.width, self.config.height)
        self.pop_window.setWindowFlag(Qt.WindowType.Popup, True)
        self.pop_window.show()

