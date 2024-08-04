import os
import re
import subprocess
from libqtile import bar, layout, hook
from libqtile.config import Match
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.config import Group, ScratchPad, DropDown, Screen
from libqtile.lazy import lazy
import layouts as custom_layouts
from utils import COLORSCHEME
import widgets as custom_widgets

home = os.path.expanduser("~")

mod = "mod4"
ctrl = "control"
shift = "shift"
alt = "mod1"
vb_command = f"{home}/.config/qtile/scripts/dunst-vb.sh"
wallpaper = f"{home}/Wallpapers/nature-of-fear.png"
rofi_script = f"{home}/.config/rofi/scripts"

widget_defaults = custom_widgets.widget_defaults
extension_defaults = custom_widgets.extension_defaults
screens = [
    Screen(
        wallpaper_mode="fill",
        wallpaper=wallpaper,
        left=bar.Bar(
            widgets=custom_widgets.widget_list,
            size=40,
            margin=[16, 0, 16, 16],
            background=COLORSCHEME["TRANSPARENT"],
        ),
    )
]

layouts = [
    custom_layouts.Scrolling(
        border_width=0,
        border_focus=COLORSCHEME["SKY"],
        border_normal=COLORSCHEME["SKY"],
        default_width=60,
        grow_amount=5,
        margin=16,
        width_rules={
            Match(wm_class="kitty"): 45,
            Match(wm_class="Zathura"): 45,
            Match(wm_class="news_flash"): 75,
            Match(wm_class="qutebrowser"): 100,
            Match(wm_class="vesktop"): 100,
            Match(wm_class="pyrogenesis"): 100,
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


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, shift], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button7", lazy.layout.scroll_right(2)),
    Click([mod], "Button6", lazy.layout.scroll_left(2)),
]

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

    Key([mod], "Semicolon", lazy.spawn("rofi -show run")),
    KeyChord([mod], "r", [
        Key([], "w", lazy.spawn("networkmanager_dmenu")),
        Key([], "b", lazy.spawn("rofi-bluetooth")),
        Key([], "c", lazy.spawn("roficlip")),
        Key([], "q", lazy.spawn("rofi -show calc")),
        Key([], "n", lazy.spawn(f"{rofi_script}/nerd-fonts.sh")),
        Key([], "z", lazy.spawn(f"{rofi_script}/zotero.sh")),
    ]),

    KeyChord([mod], "w", [
        Key([], "6", lazy.widget["v_battery"].show_popup()),
        Key([], "5", lazy.widget["v_spotify"].show_popup()),
        Key([], "4", lazy.widget["v_bright"].show_popup()),
        Key([], "3", lazy.widget["v_audio"].show_popup()),
        Key([], "2", lazy.widget["v_datetime"].show_popup()),
        Key([], "1", lazy.widget["v_power"].show_popup()),
    ]),

    Key([mod], "F9", toggle_trackpad),
    Key([ctrl, shift], "w", lazy.window.kill()),
    Key([mod, shift], "r", lazy.reload_config()),
]


opts = {
    "x": 0.2, "width": 0.6,
    "y": 0.1, "height": 0.8,
    "opacity": 1,
}
groups = [Group(str(i), label="󰝤") for i in range(1, 11)]
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
