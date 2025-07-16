import signal
import sys
from PySide6.QtWidgets import QApplication, QWidget

from pop_window import PopWindow

signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    app = QApplication(sys.argv)

    window = PopWindow("bob")
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

