import os
from libqtile.widget import base

home = os.path.expanduser("~")


class V_TextBox(base._TextBox):

    def __init__(self, **config):
        base._TextBox.__init__(self, **config)

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
