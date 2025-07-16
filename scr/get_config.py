import json
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class ButtonConfig:
    text: str
    on_click: str | None
    name: str | None

@dataclass
class Config:
    title: str
    buttons: List[ButtonConfig]
    close_on_click: bool
    no_system_border: bool
    width: int
    height: int
    animation_enabled: bool
    content_margins: Tuple
    x_offset: int
    y_offset: int

def get_config(config_path: Path):
    with open(config_path, "r") as f:
        try:
            config: Dict = json.load(f)
        except json.JSONDecodeError:
            print("Invalid config")
            sys.exit(1)

    buttons = []
    content_margins = (0, 0, 0, 0)
    margins_string: str | None = config.get("content-margins", None)

    if margins_string is not None:
        content_margins = tuple(map(int, margins_string.split(" ")))

    for json_button in config.get("buttons", []):
        button_config = ButtonConfig(
            json_button.get("text", ""),
            json_button.get("on-click", None),
            json_button.get("name", None)
        )
        buttons.append(button_config)

    config_object = Config(
            config.get("title", "pop"),
            buttons,
            config.get("close-on-click", True),
            config.get("no-system-border", False),
            config.get("width", 150),
            config.get("height", 50),
            config.get("animation", False),
            content_margins,
            config.get("x-offset", 0),
            config.get("y-offset", 0)
    )

    return config_object

