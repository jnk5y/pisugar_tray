#!/usr/bin/env python3
import os
import os.path
import sys
import socket
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import GObject as gobject
from gi.repository import GLib as glib

REFRESH_INTERVAL = 120
ICON_DIR = '/home/john/Code/pisugar_tray/images'

class PiSugarStatusTray(object):

    def __init__(self):
        self.tray = gtk.StatusIcon()
        self.tray.connect('activate', self.refresh)

        self.refresh(None)
        self.tray.set_visible(True)

        glib.timeout_add_seconds(REFRESH_INTERVAL, self.refresh, self.tray)

    def netcat(self,hostname, port, content):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((hostname,port))
            s.sendall(content)
            s.shutdown(socket.SHUT_WR)
            return_data = ''
            while 1:
                data = s.recv(1024)
                if len(data) == 0:
                    break
                return_data = data
            s.close()
            return return_data
        except Exception as e:
            print(e)
            return 'no data'
    
    def refresh(self, widget):
        try:
            b_level = 0
            b_level_tooltip = 0
            b_charging = ''
            b_file = ICON_DIR + 'Battery-Error.png'
            
            try:
                level = self.netcat('0.0.0.0',8423,b'get battery')
            except Exception as e: print(e)
            try:
                charging = self.netcat('0.0.0.0',8423,b'get battery_charging')
            except Exception as e: print(e)
            
            if charging != 'no data':
                charging = charging.decode('utf-8').strip().split(': ')[1]
                if( charging == 'true' ):
                    b_charging = '-charging'
            
            if level != 'no data':
                print( level)
                level = level.decode('utf-8').strip().split(': ')[1]
                level = round(float(level))
                b_level = level
                b_level_tooltip = level
                if( level >= 10 ):
                    b_level = b_level // 10
                    b_level = b_level * 10

                try:
                    b_file = ICON_DIR + '/Battery-' + str(b_level) + '' + b_charging + '.png'
                except Exception as e: print(e)                
            
            self.tray.set_tooltip_text(str(b_level_tooltip))
            if os.path.exists(b_file):
                self.tray.set_from_file(b_file)
            else:
                print('icon file does not exist')

        except Exception as e:
            b_file = ICON_DIR + '/Battery-Error.png'
            print(e)
            if os.path.exists(b_file):
                self.tray.set_from_file(b_file)
            else:
                print('icon file does not exist')

        return True

if __name__ == '__main__':
    app = PiSugarStatusTray()
    gtk.main()
