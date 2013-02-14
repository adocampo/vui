#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import dbus

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
