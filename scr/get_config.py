import json
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    title: str

def get_config(config_path: Path):
    with open(config_path, "r") as f:
        try:
            config: Dict = json.load(f)
        except json.JSONDecodeError:
            print("Invalid config")
            sys.exit(1)

    config_object = Config(config.get("title", "pop"))

    return config_object

