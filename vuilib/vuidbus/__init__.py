#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import gobject
gobject.threads_init()
from dbus import glib
glib.init_threads()
import dbus

#import dbus

DDESKTOP="desktop"
DSYSTEM="system"


class vuidbus:
	def __init__(self):
		#
		print ("vuidbus started")


class absdbus:
	#WARNING:
	#look for new dbus API in 0.81.0
	#
	def __init__(self):
		self.Desktop_dbus = dbus.SessionBus()
		self.System_dbus = dbus.SystemBus()

		self.rDesktopObj = self.Desktop_dbus.get_object("org.freedesktop.DBus", "/org/freedesktop/DBus")
		#self.rSystemObj = self.System_dbus.get_object("org.freedesktop.DBus", "/org/freedesktop/DBus")

	def listNames(self, busdaemon=DDESKTOP):
		if busdaemon == DDESKTOP:
			return self.rDesktopObj.ListNames()
		else:
			return self.rSystemObj.ListNames()

	def introspect(self,busdaemon=DDESKTOP):
		if busdaemon == DDESKTOP:
			return self.rDesktopObj.Introspect()
		else:
			return self.SystemObj.Introspect();

	def test(self):
		print(self.Desktop_dbus.get_object("org.freedesktop.DBus","/").Introspect())
bs
