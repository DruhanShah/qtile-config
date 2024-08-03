from qtile_extras.popup import toolkit as popup
from utils import COLORSCHEME


spotify_layout = popup.PopupAbsoluteLayout(
    width=400,
    height=200,
    controls=[
        popup.PopupImage(
            name="artwork",
            filename="~/.config/qtile/utils/none.png",
            pos_x=20,
            pos_y=20,
            width=120,
            height=120,
        ),
        popup.PopupText(
            name="title",
            font="Iosevka Etoile ExtraBold",
            fontsize=24,
            foreground=COLORSCHEME["TEXT"],
            pos_x=160,
            pos_y=40,
            width=220,
            height=40,
            h_align="left",
        ),
        popup.PopupText(
            name="artist",
            font="Iosevka Aile Medium",
            fontsize=13,
            foreground=COLORSCHEME["SUBTEXT 1"],
            pos_x=160,
            pos_y=80,
            width=220,
            height=40,
            h_align="left",
        ),
        popup.PopupSlider(
            name="progress",
            bar_size=6,
            marker_size=15,
            marker_colour=COLORSCHEME["TEXT"],
            colour_below=COLORSCHEME["GREEN"],
            colour_above=COLORSCHEME["SURFACE 0"],
            bar_border_colour=COLORSCHEME["TEXT"],
            pos_y=160,
            pos_x=20,
            height=20,
            width=360,
        ),
    ],
    background=COLORSCHEME["MANTLE"],
    close_on_click=True,
)
