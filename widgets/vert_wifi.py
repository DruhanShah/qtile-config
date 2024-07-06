import subprocess

from libqtile.log_utils import logger
from libqtile.widget import base
from libqtile.widget.wlan import get_status


def check_wired():
    result = subprocess.run(
        'cat /sys/class/net/enp*/carrier',
        shell=True,
        stdout=subprocess.PIPE
    ).stdout.splitlines()
    if len(result) == 0:
        return 0
    actual_result = 0
    for _res in result:
        actual_result += int(_res.decode('UTF-8'))
    return actual_result


class V_Internet(base.ThreadPoolText):

    orientations = base.ORIENTATION_BOTH
    defaults = [
        ("font", "sans", "Default font"),
        ("fontsize", None, "Font size"),
        ("foreground", "ffffff", "Font colour for information text"),
        ("update_interval", 1, "Polling interval in secs."),
        ("interface", "wlan0", "Name of wifi interface."),
    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "_", **config)
        self.add_defaults(V_Internet.defaults)

    def _configure(self, qtile, bar):
        base.ThreadPoolText._configure(self, qtile, bar)

    def poll(self):
        logger.debug("Polling wifi")
        wired = check_wired()
        if wired > 0:
            return "E"
        else:
            try:
                essid, quality = get_status(self.interface)
                quality = quality if essid else 0
                return "W"

            except Exception:
                logger.exception("Couldn't get wifi info.")
                return "_"

    def draw(self):
        self.drawer.clear(self.background or self.bar.background)

        self.drawer.ctx.save()

        self.layout.draw(
            (self.bar.width // 2) - (self.layout.width // 2),
            0,
        )
        self.length = self.calculate_length()
        self.drawer.draw(
            offsetx=self.offset, offsety=self.offsety,
            width=self.width, height=self.height
        )

    def calculate_length(self):
        if self.text:
            return self.layout.height + self.actual_padding * 2
        else:
            return 0
