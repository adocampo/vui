#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import fileinput, os

class mmutils:


	def __init__(self):
		self.HDMan_path = NULL
		self.HLEd_path = NULL
		self.HCopy_path = NULL
		self.HCompV_path = NULL
		self.HERest_path = NULL
		self.HHEd_path = NULL
		self.HVite_path = NULL


	def getPrompts(self, file):
		for line in fileinput.input([file]):
			lines.append([ line.split()[0] , ' '.join(line.split()[1:]) ])
		return lines

	def locateHTK (self, paths=[]):
		pass

	def setHDMan_path(self, path):
		self.HDMan_path = path
	def setHLEd_path(self, path):
		self.HLEd_path = path
	def setHCopy_path(self, path):
		self.HCopy_path = path
	def setHCompV_path(self, path):
		self.HCompV_path = path
	def setHERest_path(self, path):
		self.HERest_path = path
	def setHHEd_path(self, path):
		self.HHEd_path = path
	def setHVite_path(self, path):
		self.HVite_path = path

	def getHDMan_path(self, path):
		return self.HDMan_path
	def getHLEd_path(self, path):
		return self.HLEd_path
	def getHCopy_path(self, path):
		return self.HCopy_path
	def getHCompV_path(self, path):
		return self.HCompV_path
	def getHERest_path(self, path):
		return self.HERest_path
	def getHHEd_path(self, path):
		return self.HHEd_path
	def getHVite_path(self, path):
		return self.HVite_path









