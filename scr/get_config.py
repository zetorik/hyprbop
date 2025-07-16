import json
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ButtonConfig:
    text: str
    on_click: str | None

@dataclass
class Config:
    title: str
    buttons: List[ButtonConfig]

def get_config(config_path: Path):
    with open(config_path, "r") as f:
        try:
            config: Dict = json.load(f)
        except json.JSONDecodeError:
            print("Invalid config")
            sys.exit(1)

    buttons = []

    for json_button in config.get("buttons", []):
        button_config = ButtonConfig(
            json_button.get("text", ""),
            json_button.get("on-click", None)
        )
        buttons.append(button_config)

    config_object = Config(
            config.get("title", "pop"),
            buttons
    )

    return config_object

