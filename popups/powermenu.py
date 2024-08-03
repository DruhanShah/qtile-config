import os
from libqtile.lazy import lazy
from qtile_extras.popup import toolkit as popup
from utils import COLORSCHEME

home = os.path.expanduser("~")

powermenu_layout = popup.PopupAbsoluteLayout(
    width=420,
    height=120,
    controls=[
        popup.PopupText(
            text="",
            pos_x=20,
            pos_y=20,
            width=80,
            height=80,
            h_align="center",
            foreground=COLORSCHEME["CRUST"],
            background=COLORSCHEME["SUBTEXT 0"],
            highlight=COLORSCHEME["BLUE"],
            font="Symbols Nerd Font",
            fontsize=32,
            mouse_callbacks={
                "Button1": lazy.spawn(f"{home}/.local/bin/lock")
            },
        ),
        popup.PopupText(
            text="",
            pos_x=120,
            pos_y=20,
            width=80,
            height=80,
            h_align="center",
            foreground=COLORSCHEME["CRUST"],
            background=COLORSCHEME["SUBTEXT 0"],
            highlight=COLORSCHEME["BLUE"],
            font="Symbols Nerd Font",
            fontsize=32,
            mouse_callbacks={
                "Button1": lazy.shutdown()
            },
        ),
        popup.PopupText(
            text="",
            pos_x=220,
            pos_y=20,
            width=80,
            height=80,
            h_align="center",
            foreground=COLORSCHEME["CRUST"],
            background=COLORSCHEME["SUBTEXT 0"],
            highlight=COLORSCHEME["BLUE"],
            font="Symbols Nerd Font",
            fontsize=32,
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl reboot")
            },
        ),
        popup.PopupText(
            text="󰤆",
            pos_x=320,
            pos_y=20,
            width=80,
            height=80,
            h_align="center",
            foreground=COLORSCHEME["CRUST"],
            background=COLORSCHEME["SUBTEXT 0"],
            highlight=COLORSCHEME["BLUE"],
            font="Symbols Nerd Font",
            fontsize=32,
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl poweroff")
            },
        ),
    ],
    background=COLORSCHEME["MANTLE"],
    close_on_click=True,
)
