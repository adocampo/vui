#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import fileinput

lines = []
def VUIgetPrompts(file):
	for line in fileinput.input([file]):
		lines.append([ line.split()[0] , ' '.join(line.split()[1:]) ])
	return lines


















