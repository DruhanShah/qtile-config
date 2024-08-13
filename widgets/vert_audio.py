import subprocess
from libqtile import widget
from libqtile.widget import base
from qtile_extras.widget.mixins import ExtendedPopupMixin


class V_Audio(widget.PulseVolume, ExtendedPopupMixin):

    orientations = base.ORIENTATION_BOTH

    def __init__(self, **config):
        widget.PulseVolume.__init__(self, **config)
        ExtendedPopupMixin.__init__(self, **config)
        self.add_defaults(ExtendedPopupMixin.defaults)
        self.mouse_callbacks["Button1"] = self.show_popup

    def update_popup(self):
        mic_output = subprocess.check_output().decode("utf-8")

        out_icon = "󰕿" if self.mute else "󰕾"
        in_icon = "󰍭" if self.mute else "󰍬"

        self.extended_popup.update_controls(
            in_icon=in_icon,
            out_icon=out_icon
        )

    def _update_drawer(self):
        device_list = subprocess.check_output(
            ["bluetoothctl", "devices", "Connected"],
        )
        if device_list and "boAt Rockerz 510" in device_list.decode("utf-8"):
            self.text = self.emoji_list[4]
        elif self.volume <= 0:
            self.text = self.emoji_list[0]
        elif self.volume <= 30:
            self.text = self.emoji_list[1]
        elif self.volume <= 80:
            self.text = self.emoji_list[2]
        elif self.volume > 80:
            self.text = self.emoji_list[3]

    def calculate_length(self):
        if self.text:
            height = min(self.layout.height, self.bar.height)
            return height + self.actual_padding * 2
        else:
            return 0

    def draw(self):
        if not self.can_draw():
            return
        self.drawer.clear(self.background or self.bar.background)

        self.drawer.ctx.save()
        size = self.bar.width

        self.layout.draw(
            (size // 2) - (self.layout.width // 2),
            self.actual_padding,
        )
        self.drawer.ctx.restore()
        self.drawer.draw(
            offsetx=self.offsetx, offsety=self.offsety,
            width=self.width, height=self.height
        )
