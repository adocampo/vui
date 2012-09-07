#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import fileinput, os

class files:

	def __init__(self):
		self.HTKpath = {}
		self.HTKpath['HDMan'] = None
		self.HTKpath['HLEd'] = None
		self.HTKpath['HCopy'] = None
		self.HTKpath['HCompV'] = None
		self.HTKpath['HERest'] = None
		self.HTKpath['HHEd'] = None
		self.HTKpath['HVite'] = None

	def getPrompts(self, file):
		for line in fileinput.input([file]):
			lines.append([ line.split()[0] , ' '.join(line.split()[1:]) ])
		return lines

	def locateHTK (self, addPaths=[]):
	# This func only work with unix like
	# locateHTK is for search bin files of HTK

		osPath = os.environ["PATH"]
		if len(addPaths) > 0:
			osPath += ":" + ':'.join(addPaths)
		
		files = ['HDMan', 'HLEd', 'HCopy', 'HCompV', 'HERest', 'HHEd', 'HVite']
		paths = osPath.split(":")

		for file in files:
			for path in paths:
				if os.path.exists( os.path.join( path, file ) ):
					self.HTKpath[file] = os.path.abspath(  os.path.join( path, file )   )


	def setHDMan_path(self, path):
		self.HTKpath['HDMan'] = path
	def setHLEd_path(self, path):
		self.HTKpath['HLEd'] = path
	def setHCopy_path(self, path):
		self.HTKpath['HCopy'] = path
	def setHCompV_path(self, path):
		self.HTKpath['HCompV'] = path
	def setHERest_path(self, path):
		self.HTKpath['HERest'] = path
	def setHHEd_path(self, path):
		self.HTKpath['HHEd'] = path
	def setHVite_path(self, path):
		self.HTKpath['HVite'] = path

	def getHDMan_path(self):
		return self.HTKpath['HDMan']
	def getHLEd_path(self):
		return self.HTKpath['HLEd']
	def getHCopy_path(self):
		return self.HTKpath['HCopy']
	def getHCompV_path(self):
		return self.HTKpath['HCompV']
	def getHERest_path(self):
		return self.HTKpath['HERest']
	def getHHEd_path(self):
		return self.HTKpath['HHEd']
	def getHVite_path(self):
		return self.HTKpath['HVite']

	def getHTKbinPATH(self,bin):
		return self.HTKpath[bin]

	def setHTKbinPATH(self,bin,value):
		self.HTKpath[bin] = value

