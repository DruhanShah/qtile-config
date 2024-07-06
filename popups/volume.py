# from libqtile import widget
from qtile_extras.popup import toolkit as popup
from utils import COLORSCHEME

volume_layout = popup.PopupAbsoluteLayout(
    width=400,
    height=220,
    background=COLORSCHEME["MANTLE"],
    close_on_click=False,
    controls=[
        popup.PopupText(
            height=50,
            width=50,
            pos_x=20,
            pos_y=20,
            text="",
            # widget=widget.PulseVolume(
            #     foreground=COLORSCHEME["TEXT"],
            #     emoji=True,
            #     emoji_list=["󰝟", "󰖀", "󰕾", "󰕾"],
            #     fontsize=20,
            # ),
        ),
    ],
)
