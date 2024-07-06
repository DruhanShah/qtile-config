import os
from libqtile import qtile
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
                "Button1": lambda: qtile.spawn(f"{home}/.local/bin/lock")
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
                "Button1":
                    lambda: qtile.spawn("qtile cmd-obj -o cmd -f shutdown")
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
                "Button1": lambda: qtile.spawn("restart")
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
                "Button1": lambda: qtile.spawn("shutdown now")
            },
        ),
    ],
    background=COLORSCHEME["MANTLE"],
    close_on_click=True,
)
