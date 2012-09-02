#!/usr/bin/env python
# writed by <nache.nache@gmail.com>
# fuck this code if you want

import fileinput


all = []
for line in fileinput.input(['prompts']):
	 all = all + line.split()[1:]


all = list(set(all))

for word in sorted(all):
	print word+" ["+word+"] "+word
