For using a psion 5 keyboard on linux

The us file is found at /usr/share/X11/xkb/symbols
Copy the psion5 section and add it to your us file
Update /etc/default/keyboard to look like this and reboot:
`XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT="psion5"
XKBOPTIONS=""`
