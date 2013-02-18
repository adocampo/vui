#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import vuilib

VUIplug = vuilib.vuiplug.vuiplug()
VUIplug.loadPluginsDir("plugins/")
VUIplug.DEBUGlistPlugins()
VUIplug.sendSpeechToPlugins("test")

############## test space ################
#Lvuiconf = vuilib.vuiconf.vuiconf()

#vuiDbus= vuilib.vuidbus.absdbus()
#print(type(vuiDbus.list()))
#print vuiDbus.list()
#for cosa in vuiDbus.list():
#	print (type(cosa))
#	print (cosa);

#vuiDbus.test()
# excepcion por falta de permisos
#for cosa in vuiDbus.list("system"):
#	print (cosa)

########### end of test space ##############
