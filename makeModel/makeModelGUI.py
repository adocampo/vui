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

		layoutFiles = {}
		layoutFiles['HDMan'] = Qt.QHBoxLayout()
		layoutFiles['HLEd'] = Qt.QHBoxLayout()
		layoutFiles['HCopy'] = Qt.QHBoxLayout()
		layoutFiles['HCompV'] = Qt.QHBoxLayout()
		layoutFiles['HERest'] = Qt.QHBoxLayout()
		layoutFiles['HHEd'] = Qt.QHBoxLayout()
		layoutFiles['HVite'] = Qt.QHBoxLayout()

		self.labelFiles['HDMan'] = Qt.QLabel()
		self.labelFiles['HLEd'] = Qt.QLabel()
		self.labelFiles['HCopy'] = Qt.QLabel()
		self.labelFiles['HCompV'] = Qt.QLabel()
		self.labelFiles['HERest'] = Qt.QLabel()
		self.labelFiles['HHEd'] = Qt.QLabel()
		self.labelFiles['HVite'] = Qt.QLabel()
		
		buttonFiles['HDMan'] = Qt.QPushButton("Buscar...")
		buttonFiles['HLEd'] = Qt.QPushButton("Buscar...")
		buttonFiles['HCopy'] = Qt.QPushButton("Buscar...")
		buttonFiles['HCompV'] = Qt.QPushButton("Buscar...")
		buttonFiles['HERest'] = Qt.QPushButton("Buscar...")
		buttonFiles['HHEd'] = Qt.QPushButton("Buscar...")
		buttonFiles['HVite'] = Qt.QPushButton("Buscar...")

		self.connect(buttonFiles['HDMan'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HDMan')
		self.connect(buttonFiles['HLEd'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HLEd')
		self.connect(buttonFiles['HCopy'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HCopy')
		self.connect(buttonFiles['HCompV'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HCompV')
		self.connect(buttonFiles['HERest'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HERest')
		self.connect(buttonFiles['HHEd'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HHEd')
		self.connect(buttonFiles['HVite'], Qt.SIGNAL("clicked()"), self.FileDialog, 'HVite')


		for ['HDMan', 'HLEd', 'HCopy', 'HCompV', 'HERest', 'HHEd', 'HVite'] in binName:
			layoutFiles[binName].addWidget(Qt.QLabel(binName))
			layoutFiles[binName].addWidget(self.labelFiles[binName])
			layoutFiles[binName].addWidget(buttonFiles[binName])


		layoutV = Qt.QVBoxLayout()
		self.textEdit = Qt.QTextEdit()
		layoutV.addWidget(self.textEdit)


		for ['HDMan', 'HLEd', 'HCopy', 'HCompV', 'HERest', 'HHEd', 'HVite'] in binName:
			layoutV.addWidget(layoutFiles[binName])

		widget=Qt.QWidget()
		widget.setLayout(layoutV)

		self.setCentralWidget(widget)


	def fileDialog(self,binName):
		#Bug? if none is returnetd?
		self.labelFiles[binName] = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

	def test(self):
		print ("Killing in the name of...")


if __name__ == '__main__':
	app = Qt.QApplication(sys.argv)
	mainW = vuiGUI()
	mainW.show()
	app.exec_()
