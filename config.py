import os
import re
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Match
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.config import Group, ScratchPad, DropDown, Screen
from libqtile.lazy import lazy
import widgets as custom_widgets
import layouts as custom_layouts
import popups as custom_popups
from utils import COLORSCHEME

home = os.path.expanduser("~")

mod = "mod4"
ctrl = "control"
shift = "shift"
alt = "mod1"
vb_command = f"{home}/.config/qtile/scripts/dunst-vb.sh"
wallpaper = f"{home}/Wallpapers/neuschwanstein.jpg"
rofi_script = f"{home}/.config/rofi/scripts"


@lazy.function
def toggle_trackpad(qtile):
    status = subprocess.check_output(["xinput", "list-props", "10"])
    status = status.decode("utf-8")
    status = re.search(r"Device Enabled.*(\d)", status)
    status = status.group(1)

    if status == "1":
        subprocess.run(["xinput", "disable", "10"])
    else:
        subprocess.run(["xinput", "enable", "10"])


keys = [
    Key([], "XF86MonBrightnessUp", lazy.spawn(f"{vb_command} bright_up")),
    Key([], "XF86MonBrightnessDown", lazy.spawn(f"{vb_command} bright_down")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f"{vb_command} vol_up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(f"{vb_command} vol_down")),
    Key([], "XF86AudioMute", lazy.spawn(f"{vb_command} volume_mute")),
    Key([], "XF86AudioPlay", lazy.spawn(f"{vb_command} play_pause")),
    Key([], "print", lazy.spawn("flameshot gui")),

    Key([mod], "space", lazy.layout.next()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, shift], "h", lazy.layout.shuffle_left()),
    Key([mod, shift], "j", lazy.layout.shuffle_down()),
    Key([mod, shift], "k", lazy.layout.shuffle_up()),
    Key([mod, shift], "l", lazy.layout.shuffle_right()),
    Key([mod, ctrl, shift], "h", lazy.layout.shrink_left()),
    Key([mod, ctrl, shift], "j", lazy.layout.grow_down()),
    Key([mod, ctrl, shift], "k", lazy.layout.shrink_up()),
    Key([mod, ctrl, shift], "l", lazy.layout.grow_right()),
    Key([mod, ctrl], "h", lazy.layout.scroll_left()),
    Key([mod, ctrl], "l", lazy.layout.scroll_right()),
    Key([mod, ctrl], "equal", lazy.layout.reset_scroll()),

    Key([mod, shift], "space", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    Key([mod], "Return", lazy.spawn("kitty")),
    Key([mod], "b", lazy.spawn("qutebrowser")),

    Key([mod], "Semicolon", lazy.spawn(f"{rofi_script}/launcher.sh")),
    KeyChord([mod], "r", [
        Key([], "w", lazy.spawn(f"{rofi_script}/wifi.sh")),
        Key([], "b", lazy.spawn(f"{rofi_script}/bluetooth.sh")),
        Key([], "c", lazy.spawn(f"{rofi_script}/clipboard.sh")),
        Key([], "q", lazy.spawn(f"{rofi_script}/calculator.sh")),
        Key([], "n", lazy.spawn(f"{rofi_script}/nerd-fonts.sh")),
        Key([], "z", lazy.spawn(f"{rofi_script}/zotero.sh")),
        Key([], "6", lazy.spawn(f"{rofi_script}/battery.sh")),
        Key([], "5", lazy.spawn(f"{rofi_script}/spotify.sh")),
        Key([], "4", lazy.spawn(f"{rofi_script}/brightness.sh")),
        Key([], "3", lazy.spawn(f"{rofi_script}/volume.sh")),
        Key([], "2", lazy.spawn(f"{rofi_script}/calendar.sh")),
        Key([], "1", lazy.spawn(f"{rofi_script}/powermenu.sh")),
    ]),
    Key([mod], "q", lazy.spawn(f"{rofi_script}/powermenu.sh")),

    Key([mod], "F9", toggle_trackpad),
    Key([ctrl, shift], "w", lazy.window.kill()),
    Key([mod, shift], "r", lazy.reload_config()),
]

opts = {
    "x": 0.2, "width": 0.6,
    "y": 0.1, "height": 0.8,
    "opacity": 1,
}
groups = [Group(str(i), label="󱓻") for i in range(1, 11)]
scratch_names = ["Music", "Diagnostics"]
scratch_commands = ["spotify", "kitty -e 'btop'"]
scratch_keys = ["m", "d"]

for group in groups:
    name = group.name
    key = name[-1]
    keys.append(Key([mod], key, lazy.group[name].toscreen(toggle=True)))
    keys.append(Key([mod, shift], key, lazy.window.togroup(name)))

groups.append(ScratchPad("scratch", [
    DropDown(name, command, **opts)
    for name, command in zip(scratch_names, scratch_commands)
]))

for name, key in zip(scratch_names, scratch_keys):
    keys.append(Key([mod], key, lazy.group["scratch"].dropdown_toggle(name)))


widget_defaults = dict(
    font="Symbols Nerd Font",
    fontsize=16,
    padding=0,
    foreground=COLORSCHEME["TEXT"],
    background=COLORSCHEME["BASE"],
)
extension_defaults = widget_defaults.copy()

widget_list = [
    custom_widgets.V_GroupBox(
        highlight_method="text",
        active=COLORSCHEME["TEXT"],
        inactive=COLORSCHEME["SURFACE 1"],
        urgent_text=COLORSCHEME["RED"],
        this_current_screen_border=COLORSCHEME["BLUE"],
        this_screen_border=COLORSCHEME["BLUE"],
        other_current_screen_border=COLORSCHEME["YELLOW"],
        other_screen_border=COLORSCHEME["YELLOW"],
        padding=6,
        font="JetBrains Mono ExtraBold",
        fontsize=20,
        margin_x=1,
    ),
    widget.Spacer(),
    custom_widgets.V_Battery(
        popup_layout=custom_popups.battery_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 12,
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
    custom_widgets.V_Spotify(
        popup_layout=custom_popups.spotify_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 12,
            "y": -140,
        },
        text="",
        foreground=COLORSCHEME["GREEN"],
        fontsize=20,
        padding=5,
    ),
    custom_widgets.V_Bright(
        popup_layout=custom_popups.bright_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 12,
            "y": -140,
        },
        text="󰃟",
        foreground=COLORSCHEME["MAUVE"],
        fontsize=20,
        padding=5,
    ),
    custom_widgets.V_Audio(
        popup_layout=custom_popups.volume_layout,
        popup_hide_timeout=2,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 12,
            "y": -120,
        },
        foreground=COLORSCHEME["FLAMINGO"],
        emoji=True,
        emoji_list=["󰝟", "󰖀", "󰕾", "󰕾", "󰋋"],
        fontsize=20,
        padding=5,
    ),
    custom_widgets.V_DateTime(
        popup_layout=custom_popups.calendar_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 12,
            "y": -12,
        },
        format="%H\n%M\n%S",
        foreground=COLORSCHEME["LAVENDER"],
        font="JetBrains Mono SemiBold",
        fontsize=20,
        padding=10,
    ),
    custom_widgets.V_Power(
        popup_layout=custom_popups.powermenu_layout,
        popup_hide_timeout=0,
        popup_show_args={
            "relative_to": 7,
            "relative_to_bar": True,
            "x": 12,
            "y": -12,
        },
        text="",
        foreground=COLORSCHEME["RED"],
        fontsize=20,
        padding=10,
    ),
]

screens = [
    Screen(
        wallpaper_mode="fill",
        wallpaper=wallpaper,
        left=bar.Bar(
            widgets=widget_list,
            size=36,
            margin=[12, 0, 12, 12],
        ),
    )
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, shift], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button7", lazy.layout.scroll_right(2)),
    Click([mod], "Button6", lazy.layout.scroll_left(2)),
]


layouts = [
    custom_layouts.Scrolling(
        border_width=0,
        border_focus=COLORSCHEME["SKY"],
        border_normal=COLORSCHEME["SKY"],
        default_width=60,
        grow_amount=5,
        margin=12,
        width_rules={
            Match(wm_class="kitty"): 48,
            Match(wm_class="Zathura"): 48,
            Match(wm_class="qutebrowser"): 100,
            Match(wm_class="vesktop"): 100,
        },
    ),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(title="file-picker"),
        Match(wm_class="matplotlib"),
    ],
    border_focus=COLORSCHEME["SKY"],
    border_normal=COLORSCHEME["SKY"],
    border_width=0,
)


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "QTile"
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([f"{home}/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.client_new
def resize(window):
    if window.match(Match(wm_class="mpv")):
        window.cmd_set_size_floating(1600, 900)
    if window.match(Match(title="file-picker")):
        window.cmd_set_size_floating(1280, 720)