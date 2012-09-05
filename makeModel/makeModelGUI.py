#!/usr/bin/env python
# Writed by J.A. NachE <nache.nache@gmail.com>
# Under one license, ask me for more information.

import sys, os
sys.path.append(os.path.abspath(os.path.dirname(sys.argv[0])))
from vuilib import mmutils
from PyQt4 import Qt

class vuiGUI(Qt.QMainWindow):
	def __init__ (self):

		super(vuiGUI, self).__init__(None)	
		self.setWindowTitle("make Model GUI")

		HTKbins=['HDMan', 'HLEd', 'HCopy', 'HCompV', 'HERest', 'HHEd', 'HVite']

		layoutFiles = {}
		self.labelFiles = {}
		buttonFiles = {}
		layoutV = Qt.QVBoxLayout()
		self.textEdit = Qt.QTextEdit()
		layoutV.addWidget(self.textEdit)

		for binName in HTKbins:
			layoutFiles[binName] = Qt.QHBoxLayout()
			self.labelFiles[binName] = Qt.QLabel()	
			buttonFiles[binName] = Qt.QPushButton("Buscar...")
			self.connect(buttonFiles[binName], Qt.SIGNAL("clicked()"), lambda bnam=binName: self.FileDialog(bnam))

			layoutFiles[binName].addWidget(Qt.QLabel(binName))
			layoutFiles[binName].addWidget(self.labelFiles[binName])
			layoutFiles[binName].addWidget(buttonFiles[binName])

			layoutV.addLayout(layoutFiles[binName])

		widget=Qt.QWidget()
		widget.setLayout(layoutV)

		self.setCentralWidget(widget)


	def FileDialog(self,binName):
		#Bug? if none is returnetd?
		selectedFile = Qt.QFileDialog.getOpenFileName(self, 'Buscar binario '+binName, '/home')
		self.labelFiles[binName].setText(selectedFile)


if __name__ == '__main__':
	app = Qt.QApplication(sys.argv)
	mainW = vuiGUI()
	mainW.show()
	app.exec_()
