#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import vuilib



############## test space ################
Lvuiconf = vuilib.vuiconf.vuiconf()


vuiDbus= vuilib.vuidbus.absdbus()
print(type(vuiDbus.list()))
print vuiDbus.list()
for cosa in vuiDbus.list():
	print cosa

########### end of test space ##############
