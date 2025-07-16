import signal
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from get_config import get_config

from pop_window import PopWindow

signal.signal(signal.SIGINT, signal.SIG_DFL)

CONFIG_PATHS = [Path("~/.config/hyprpop/") , Path(__file__).parent.parent / "config"]

def main() -> None:
    if len(sys.argv) < 2:
        print("hyprpop: Please provide a config name")
        sys.exit(1)

    config_name = sys.argv[1]
    json_config = None

    for config_path in CONFIG_PATHS:
        json_config = config_path / (config_name + ".json")

        print(json_config)

        if json_config.exists():
            break

    if json_config is None or not json_config.exists():
        print("hyprpop: Specified config file does not exist")
        sys.exit(1)

    config = get_config(json_config)

    app = QApplication(sys.argv)

    window = PopWindow(config)
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

