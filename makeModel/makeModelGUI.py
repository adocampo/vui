#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.


import sys
from PyQt4 import Qt

class vuiGUI(Qt.QMainWindow):
	def __init__ (self):

		super(vuiGUI, self).__init__(None)	
		self.setWindowTitle("make Model GUI")

		layoutV = Qt.QVBoxLayout()
		layoutV.addWidget(Qt.QLabel("Test"))
		self.button =  Qt.QPushButton("Test")
		self.connect(self.button, Qt.SIGNAL("clicked()"), self.test)
		layoutV.addWidget(self.button)

		widget=Qt.QWidget()
		widget.setLayout(layoutV)

		self.setCentralWidget(widget)


	def test(self):
		print "Killing in the name of..."


if __name__ == '__main__':
	app = Qt.QApplication(sys.argv)
	mainW = vuiGUI()
	mainW.show()
	app.exec_()
