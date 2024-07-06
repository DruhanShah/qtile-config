from libqtile import widget
from libqtile.widget import base
from qtile_extras.widget.mixins import ExtendedPopupMixin
import psutil


def sec2hr(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return f"{h}:{m}:{s}"


def get_icon(value):
    if 0 <= value < 0.2:
        return "󰁺"
    if 0.2 <= value < 0.4:
        return "󰁼"
    if 0.4 <= value < 0.6:
        return "󰁾"
    if 0.6 <= value < 0.8:
        return "󰂀"
    if 0.8 <= value <= 1:
        return "󰂂"
    return "󰂑"


class V_Battery(widget.Battery, ExtendedPopupMixin):

    orientation = base.ORIENTATION_BOTH

    def __init__(self, **config):
        widget.Battery.__init__(self, **config)
        ExtendedPopupMixin.__init__(self, **config)
        self.add_defaults(ExtendedPopupMixin.defaults)
        self.add_callbacks({"Button1": self.show_popup})

    def update_popup(self):
        icon = ""
        percentage = "0%",
        value = 0
        charging = "Charging"

        battery = psutil.sensors_battery()
        percentage = f"{round(battery.percent, 2)}%"
        value = battery.percent / 100
        if battery.power_plugged:
            charging = "Charging" if battery.percent < 100 else "Charged"
            icon = "󰂄" if battery.percent < 100 else "󱟢"
        else:
            charging = f"Discharging. Reaches 0% in {sec2hr(battery.secsleft)}"
            icon = get_icon(value)

        self.extended_popup.update_controls(
            icon=icon,
            percentage=percentage,
            value=value,
            charging=charging,
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
            0,
        )
        self.drawer.ctx.restore()
        self.drawer.draw(
            offsetx=self.offsetx, offsety=self.offsety,
            width=self.width, height=self.height
        )
