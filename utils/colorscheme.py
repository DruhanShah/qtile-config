from catppuccin import PALETTE
import os

file = os.path.expanduser("~/.config/qtile/theme")
with open(file, "r") as f:
    theme = f.read().strip()

COLORSCHEME = {}

COLORSCHEME["TRANSPARENT"] = "00000000"
pal = PALETTE.latte.colors if theme == "latte" else PALETTE.mocha.colors
for color in pal:
    COLORSCHEME[color.name.upper()] = color.hex
