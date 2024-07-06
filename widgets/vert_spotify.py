import os
from libqtile.widget import base
from qtile_extras.widget.mixins import ExtendedPopupMixin
from gi.repository import Playerctl
from urllib.parse import urlparse

home = os.path.expanduser("~")


class V_Spotify(base._TextBox, ExtendedPopupMixin):

    def __init__(self, **config):
        base._TextBox.__init__(self, **config)
        ExtendedPopupMixin.__init__(self, **config)
        self.add_defaults(ExtendedPopupMixin.defaults)
        self.add_callbacks({"Button1": self.show_popup})

    def update_popup(self):
        manager = Playerctl.PlayerManager()
        names = manager.props.player_names
        none = False
        for name in names:
            if name.name == "spotify":
                player = Playerctl.Player.new_from_name(name)
                metadata = player.props.metadata
                break
        else:
            none = True

        if none:
            title = "No music playing"
            artist = "Start playing music to see info"
            artUrl = f"{home}/.config/qtile/utils/none.png"
            value = 0
        else:
            title = metadata["xesam:title"]
            artist = metadata["xesam:artist"][0]
            parse = urlparse(metadata["mpris:artUrl"])
            artUrl = f"{parse.scheme}://{parse.netloc}{parse.path}"

            position = player.props.position
            length = metadata["mpris:length"]
            value = position / length

        self.extended_popup.update_controls(
            artwork=artUrl,
            title=title,
            artist=artist,
            progress=value,
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
