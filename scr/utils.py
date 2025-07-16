import os
import subprocess
import threading


def set_window_prop(prop: str, value: str):
    subprocess.run(["hyprctl",
                    "dispatch",
                    "setprop",
                    f"pid:{os.getpid()}",
                    prop,
                    value])


def get_cursor_pos() -> tuple[int, int]:
    out = subprocess.run(["hyprctl", "cursorpos"], capture_output=True, text=True).stdout

    cords = out.split(", ")
    cords = list(map(int, cords))

    return cords[0], cords[1] 


def raw_move_window(x: int, y: int, inf: bool=False) -> None:
    pid = os.getpid()

    #hyprctl dispatch setprop pid:25956 noanim 1 

    result = None

    while inf or result != "ok\n":
        set_window_prop("noanim", "1")

        result = subprocess.run(["hyprctl",
                    "dispatch",
                    "movewindowpixel",
                    "exact",
                    str(x), str(y)+",",
                    f"pid:{pid}"], capture_output=True, text=True).stdout


def move_window(x: int, y: int) -> None:
    thread = threading.Thread(target=lambda: raw_move_window(x, y))

    thread.start()

