For using a psion 5 keyboard on linux

The us file is found at /usr/share/X11/xkb/symbols
Copy the psion5 section and add it to your us file
Update /etc/default/keyboard to look like this and reboot:
`XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT="psion5"
XKBOPTIONS=""`

Learned a lot here https://www.charvolant.org/doug/xkb/html/node5.html#Sec:SymbolsModifiers and https://help.ubuntu.com/community/Custom%20keyboard%20layout%20definitions
