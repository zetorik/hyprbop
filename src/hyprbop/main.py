#!/bin/python3
import signal
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from hyprbop.get_config import get_config
from hyprbop.pop_holder import PopHolder

signal.signal(signal.SIGINT, signal.SIG_DFL)

CONFIG_PATHS = [Path("~/.config/hyprpop/") , Path(__file__).parent.parent / "config"]

def load_stylesheet(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def main() -> None:
    print(__file__)
    if len(sys.argv) < 2:
        print("hyprpop: Please provide a config name")
        sys.exit(1)

    config_name = sys.argv[1]
    json_config = None
    style = None

    for config_path in CONFIG_PATHS:
        json_config = config_path / (config_name + ".json")

        if json_config.exists():
            break

    for config_path in CONFIG_PATHS:
        base_style = config_path / "style.qss"
        custom_style = config_path / (config_name + ".qss")

        if custom_style.exists():
            style = load_stylesheet(custom_style)
        elif base_style.exists():
            style = load_stylesheet(base_style)

        if style is not None:
            break

    if json_config is None or not json_config.exists():
        print("hyprpop: Specified config file does not exist")
        sys.exit(1)

    config = get_config(json_config)

    app = QApplication(sys.argv)

    if style is not None:
        app.setStyleSheet(style)

    window = PopHolder(config)
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

