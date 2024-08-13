import os
import subprocess
from libqtile.widget import base
from qtile_extras.widget.mixins import ExtendedPopupMixin

home = os.path.expanduser("~")


class V_Bright(base._TextBox, ExtendedPopupMixin):

    def __init__(self, **config):
        base._TextBox.__init__(self, **config)
        ExtendedPopupMixin.__init__(self, **config)
        self.add_defaults(ExtendedPopupMixin.defaults)
        self.add_callbacks({"Button1": self.show_popup})

    def update_popup(self):
        g = subprocess.check_output(["brightnessctl", "g"]).decode("utf-8")
        m = subprocess.check_output(["brightnessctl", "m"]).decode("utf-8")
        val = round(int(g) / int(m), 3)
        percent = f"{int(val * 100)}%"

        with open(f"{home}/.config/qtile/theme", "r") as f:
            theme = f.read().strip()
        if theme == "latte":
            mode_str = "Light mode"
            icon = "󰃠"
        else:
            mode_str = "Dark mode"
            icon = "󰃜"

        self.extended_popup.update_controls(
            percent=percent,
            value=val,
            mode=mode_str,
            icon=icon,
        )

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
