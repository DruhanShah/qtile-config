from libqtile import widget
import popups as custom_popups
from utils import COLORSCHEME

from .vert_datetime import V_DateTime
from .vert_group import V_GroupBox
from .vert_battery import V_Battery
from .vert_audio import V_Audio
# from .vert_wifi import V_Internet
from .vert_powermenu import V_Power
from .vert_spotify import V_Spotify
from .vert_brightness import V_Bright
from .vert_textbox import V_TextBox

widget_defaults = dict(
    font="Symbols Nerd Font",
    fontsize=16,
    padding=0,
    foreground=COLORSCHEME["TEXT"],
    background=COLORSCHEME["BASE"],
)
extension_defaults = widget_defaults.copy()

widget_list = [
    widget.TextBox(),
    V_GroupBox(
        highlight_method="text",
        active=COLORSCHEME["TEXT"],
        inactive=COLORSCHEME["SURFACE 1"],
        urgent_text=COLORSCHEME["RED"],
        this_current_screen_border=COLORSCHEME["BLUE"],
        this_screen_border=COLORSCHEME["BLUE"],
        other_current_screen_border=COLORSCHEME["YELLOW"],
        other_screen_border=COLORSCHEME["YELLOW"],
        padding=2,
        fontsize=21,
    ),
    widget.TextBox(),
    widget.Spacer(
        background=COLORSCHEME["TRANSPARENT"],
    ),
    widget.TextBox(),
    V_Battery(
        popup_layout=custom_popups.battery_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 16,
            "y": -240,
        },
        format="{char}",
        charge_char="󰂄",
        discharge_char="󰁾",
        full_char="󱟢",
        show_short_text=False,
        foreground=COLORSCHEME["TEAL"],
        low_foreground=COLORSCHEME["RED"],
        low_percentage=0.2,
        fontsize=20,
        padding=5,
    ),
    V_Spotify(
        popup_layout=custom_popups.spotify_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 16,
            "y": -140,
        },
        text="",
        foreground=COLORSCHEME["GREEN"],
        fontsize=20,
        padding=5,
    ),
    V_Bright(
        popup_layout=custom_popups.bright_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 16,
            "y": -140,
        },
        text="󰃟",
        foreground=COLORSCHEME["MAUVE"],
        fontsize=20,
        padding=5,
    ),
    V_Audio(
        popup_layout=custom_popups.volume_layout,
        popup_hide_timeout=2,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 16,
            "y": -120,
        },
        foreground=COLORSCHEME["FLAMINGO"],
        emoji=True,
        emoji_list=["󰝟", "󰖀", "󰕾", "󰕾", "󰋋"],
        fontsize=20,
        padding=5,
    ),
    widget.TextBox(),
    V_TextBox(background=COLORSCHEME["TRANSPARENT"]),
    V_DateTime(
        popup_layout=custom_popups.calendar_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 16,
            "y": -16,
        },
        format="%H\n%M\n%S",
        foreground=COLORSCHEME["TEXT"],
        font="Iosevka Slab Medium",
        fontsize=22,
        padding=10,
    ),
    V_TextBox(background=COLORSCHEME["TRANSPARENT"]),
    V_Power(
        popup_layout=custom_popups.powermenu_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 16,
            "y": -16,
        },
        text="",
        foreground=COLORSCHEME["RED"],
        fontsize=20,
        padding=15,
    ),
]
