#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import fileinput

class mmutils:

	def getPrompts(self, file):
		for line in fileinput.input([file]):
			lines.append([ line.split()[0] , ' '.join(line.split()[1:]) ])
		return lines

	def locateHTK (self):
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

