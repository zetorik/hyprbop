import os
import signal
import sys
from PySide6.QtWidgets import QApplication
from utils import get_cursor_pos, move_window

from pop_window import PopWindow

signal.signal(signal.SIGINT, signal.SIG_DFL)

def main() -> None:
    app = QApplication(sys.argv)

    window1 = PopWindow("bob")
    window1.show()

    app.exec()

if __name__ == "__main__":
    main()

