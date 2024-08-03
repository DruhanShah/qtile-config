import calendar
import datetime
import re
from libqtile import widget
from libqtile.widget import base
from qtile_extras.widget.mixins import ExtendedPopupMixin
from utils import COLORSCHEME


class V_DateTime(widget.Clock, ExtendedPopupMixin):

    orientation = base.ORIENTATION_BOTH

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        ExtendedPopupMixin.__init__(self, **config)
        self.add_defaults(ExtendedPopupMixin.defaults)
        self.add_callbacks({"Button1": self.show_popup})

    def update_popup(self):
        today = datetime.date.today()
        cal = calendar.TextCalendar()
        s = cal.formatmonth(today.year, today.month, w=3).split("\n")
        weekdays, cal = s[1], s[2:]

        if len(cal[-1]) < len(cal[1]):
            cal[-1] += " "*(len(cal[1])-len(cal[-1]))
        for i, week in enumerate(cal):
            cal[i] = re.sub(
                rf"\b({today.day})\b",
                rf'<span color="{COLORSCHEME["RED"]}"><b>\1</b></span>',
                week
            )

        s = "\n".join(cal)

        month_str = today.strftime("%B")
        today_str = f"{today.day} {month_str}"
        today_day = f"{today.strftime('%A').upper()}"
        self.extended_popup.update_controls(
            todate=today_str,
            today=today_day,
            weekdays=weekdays,
            calendar=s,
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
