import os, imp
class vuiplug:
	def __init__(self):
		self.plugins = []
		self.instancedPlugins = []

	def loadPluginsDir(self,path):
		for filename in os.listdir(path):
			print("[+] Loading "+path+filename)
			self.plugins.append(imp.load_module(filename, *imp.find_module(filename, [path+filename])))
			#self.plugins[-1] the last element
			try:
				plug_class = getattr(self.plugins[-1], filename) # filename = class name
				self.instancedPlugins.append( plug_class() )
			except AttributeError:
				print ("[!] Error: main class from plugin "+filename+" not found")

	def sendSpeechToPlugins(self,speech):
		for plug in self.instancedPlugins:
			try:
				plug.speech(speech)
			except AttributeError:
				print("[!] Error: mising speech method on plugin")

	def DEBUGlistPlugins(self):
		for plug in self.plugins:
			print plug

		for plug in self.instancedPlugins:
			print plug
