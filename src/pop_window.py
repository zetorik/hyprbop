import sys
from functools import partial
import os
from PySide6.QtCore import  Qt, Signal
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QPushButton
from get_config import Config

class PopWindow(QWidget):
    closing = Signal()

    def __init__(self, config: Config) -> None:
        super().__init__()
    
        self.config = config

        self.setWindowTitle(config.title)
        self.setFixedSize(2, 2)
        self.setContentsMargins(*config.content_margins)

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.setObjectName("PopWindow")

        for button_config in config.buttons:
            button = QPushButton(button_config.text)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            if button_config.name is not None:
                button.setObjectName(button_config.name)

            self.main_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

            if button_config.on_click is not None:
                button.clicked.connect(partial(self.on_click, button, button_config.on_click))

    def on_click(self, button: QPushButton, command: str) -> None:
        os.system(command)

        if self.config.close_on_click:
            sys.exit(0)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.closing.emit()

