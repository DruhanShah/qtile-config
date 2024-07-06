#!/bin/sh

# Input device shenanigans
xinput set-prop 10 344 1
xinput set-prop 10 317 1
xinput set-prop 10 352 0
setxkbmap -option ctrl:swapcaps
xcape -e 'Control_L=Escape'

# Autostart programs
clipster -d &
picom &
rclone --vfs-cache-mode writes mount OneDrive: ~/OneDrive
