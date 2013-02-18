#!/usr/bin/env python
# Writed by J.A. Nache <nache.nache@gmail.com>
# This code is licensed under GPLv3

########### Librerias y funciones ################
import os, sys
from subprocess import Popen
import socket
import time
from xml.dom.minidom import parseString
from time import gmtime, strftime
import vuilib

VUIplug = vuilib.vuiplug.vuiplug()
VUIplug.loadPluginsDir("plugins/") #this path need to be extracted from config file

class JulConnect:
	
	def __init__(self, host, port):
		#### nos conectamos con julius y esperamos a recibir XML ####
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((host, port))
		self.sleep=0;
		#self.DsessBus = dbus.SessionBus();
		self.mainLoop()
		
	def mainLoop(self):
		dataBuild=''
		while 1:	
			data = self.sock.recv(512)
			if data.rstrip()[-1] == ".":
				self.parseXMLugly(dataBuild+data)
				dataBuild=''
			else:
				dataBuild += data
			
	def send(self,msg):
		self.sock.send(msg)

	def parseXMLugly(self, data):
		###debug
		#print data
		###debug

		for toParse in data.split(".\n"):
			toParse = toParse.replace("<s>","s").replace("</s>","/s")
			dom = parseString("<root>"+toParse+"</root>")
			if len(dom.getElementsByTagName('INPUT')) >= 1:
				status = dom.getElementsByTagName('INPUT')[0].getAttribute("STATUS")
				if status == "LISTEN":
					print ("Waiting for speech...")
				elif status == "STARTREC":
					print "Speech detected, recording..."
				elif status == "ENDREC":
					print ("End of speech.")
			elif len(dom.getElementsByTagName('STARTRECOG')) >= 1:
				print ("Starting Recognition")
			elif len(dom.getElementsByTagName('ENDRECOG')) >= 1:
				print ("Ended Recognition")
			elif len(dom.getElementsByTagName('RECOGOUT')) >= 1:
				command=""
				for node in dom.getElementsByTagName('WHYPO'):
					if node.getAttribute('WORD') != 's' and node.getAttribute('WORD') != '/s':
						command += " "+node.getAttribute('WORD')
				print ("Received:", command)
				print ("Sending "+command+" to plugins")
				VUIplug.sendSpeechToPlugins(command)
				#self.execCommands(command)

	#obsolete
	def execCommands(self, command):
	## Vale, aqui por ahora unos pocos if/else, pero este
	## deberia ser el nucleo de la IA, donde aprenda
	## y se creen condicionales de forma automatica
	## se podrian generar .grammar y .voca ya que
	## se pueden cambiar en vivo (eso dice la documentacion)
	## http://julius.sourceforge.jp/juliusbook/en/jcontrol.html
	## Seccion Grammar handling
	
		command = command.strip()
	
		if command == "SLEEP COMPUTER":
			if self.sleep == 0:
				self.sock.send("PAUSE\n")
				os.system("echo durmiendo | /usr/bin/festival --tts");
				self.sock.send("RESUME\n")
				self.sleep = 1
	
		if command == "WAKE UP COMPUTER":
			self.sock.send("PAUSE\n")
			os.system("echo si? | /usr/bin/festival --tts");
			self.sock.send("RESUME\n")
			self.sleep = 0
			
		if self.sleep == 0:	
			if command == "RUN PROGRAM ONE" or command == "RUN ONE":
				self.pone = Popen(['vlc'])
			elif command == "CLOSE PROGRAM ONE" or command == "CLOSE ONE":
				self.pone.terminate()
			elif command == "TIME IN SPAIN":
				self.sock.send("PAUSE\n")
				os.system("echo "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+" | /usr/bin/festival --tts");
				self.sock.send("RESUME\n")
			elif command == "STOP ONE":
				proxy = self.DsessBus.get_object('org.mpris.MediaPlayer2.vlc','/org/mpris/MediaPlayer2')
				dbus.Interface(proxy, 'org.mpris.MediaPlayer2.Player.Stop')
			elif command == "PLAY ONE":
				proxy = self.DsessBus.get_object('org.mpris.MediaPlayer2.vlc','/org/mpris/MediaPlayer2')
				dbus.Interface(proxy, 'org.mpris.MediaPlayer2.Player.Play')
			else:
				print "Palabra no registrada: ", command

				
		else:
			print "ZzzZZzz..."
			
			
		

##################################################




#### arrancamos julius ####
print "Arrancando julius"
jPid = Popen(['./julius', '-C', 'Sample.jconf'])

#### esperamos un poquito a que julius arranque ####
#### cutre, pero poco a poco ####
time.sleep(5)

try:
	jul = JulConnect('localhost', 10500)
	
except KeyboardInterrupt:
	print "\nSaliendo...\n"
	jPid.terminate()
	sys.exit()





