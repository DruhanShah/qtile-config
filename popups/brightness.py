from libqtile import qtile
from qtile_extras.popup import toolkit as popup
from utils import COLORSCHEME


def drag_callback(x):
    qtile.spawn(f"brightnessctl set {round(x * 100)}%")


bright_layout = popup.PopupAbsoluteLayout(
    width=400,
    height=120,
    controls=[
        popup.PopupText(
            name="icon",
            font="Symbols Nerd Font",
            fontsize=25,
            foreground=COLORSCHEME["TEXT"],
            pos_x=20,
            pos_y=40,
            width=30,
            height=20,
            h_align="center",
        ),
        popup.PopupText(
            name="percent",
            font="Fira Sans Bold",
            fontsize=18,
            foreground=COLORSCHEME["TEXT"],
            pos_x=50,
            pos_y=40,
            width=70,
            height=20,
            h_align="center",
        ),
        popup.PopupText(
            name="mode",
            font="Fira Sans",
            fontsize=14,
            foreground=COLORSCHEME["SUBTEXT 1"],
            pos_x=130,
            pos_y=60,
            width=240,
            height=20,
            h_align="center",
        ),
        popup.PopupSlider(
            name="value",
            bar_size=8,
            marker_size=12,
            marker_colour=COLORSCHEME["TEXT"],
            colour_below=COLORSCHEME["MAUVE"],
            colour_above=COLORSCHEME["SURFACE 0"],
            bar_border_colour=COLORSCHEME["TEXT"],
            pos_x=120,
            pos_y=40,
            height=20,
            width=260,
            can_focus=True,
            highlight=COLORSCHEME["MANTLE"],
            drag_callback=drag_callback,
        ),
    ],
    background=COLORSCHEME["MANTLE"],
    initial_focus=3,
    close_on_click=False,
)