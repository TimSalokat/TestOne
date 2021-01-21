#only works on linux
import os

def com(command):
	os.system(command)

cwd = os.getcwd()
	
#change into the directory from ngrok	
os.chdir (cwd + "/TestOne/TimCodesShit/Projects/comServerClient/commandsPhoneLaptop")

#change authtoken to baumkeks28
com("./ngrok authtoken 1guUHSx9M6Op9fTSbRXdAVgc4FN_3qFbrCjQAauJVQ6DN4qbo")

#start ngrok service on tcp localhost and port 1234
com("gnome-terminal -x ./ngrok tcp 127.0.1.1:1234 ")
