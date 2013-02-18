
#This is a sample plugin
#The name of the dir, file and the class need to be the same
class VUIsample:
	#here the construct method
	def __init__(self):
		print("sample plugin")


	#here the main program send the speech registered
	def speech(self,speech):
		print("you say " + speech)
		#here I do something
