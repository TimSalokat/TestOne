#!/bin/python3 

#TODO 
#
#
#
#

#Import
import os
import speech_recognition as sr
import pyaudio
import text_to_speech as speech
from termcolor import colored
import random
import datetime as dt

#init stuff
r = sr.Recognizer()

#Defining Variables
theUltimatePath = "/home/parrot/Documents/Python/Projects/Tilih/"
comServerPath = "/home/parrot/Documents/Python/Projects/comServerClient/commandsPhoneLaptop/comServer.py"

show = True
schleife = True
lastInput = "None"
comLog = []
words = []
wordListPath = theUltimatePath + "words.txt"
comLogPath = theUltimatePath + "comLog.txt"

#wörter welche vom eingabe string entfernt werden.
with open(wordListPath) as file:
	for line in file:
		for word in line.split():
			words.append(word)

#---------------------------------------------

#Print but cleaner 
def debug(Message = "Debug", color = "green"):
	if show == False and color != "cyan":
		return 0
	else:
		print(colored("Debug: ", color) + Message)

#Do you want to show the debug messages? idk why i make a funtion for this
def ShowDebug():
	YesOrNo = input("Do you want to show the Debug? Y/N: ")
	if YesOrNo == "n" or YesOrNo == "N":
		print(colored("Not showing debug messages.", "green"))
		global show	
		show = False
	else:
		print(colored("Showing debug messages.", "green"))
		return 0

#Do you want to show the debug messages? idk why i make a funtion for this
def TextOrSpeech():
	#Yes/True = Text and No/False = Speech	
	YesOrNo = input("Do you want to input by text? Y/N: ")
	if YesOrNo.lower() == "n":
		debug("Taking input by speech.")
		global TextOrSpeech	
		TextOrSpeech = False
	else:
		debug("Taking input by text.")
		TextOrSpeech = True

#Input from the user 
def Input(msg = colored(":~: ", "cyan")):
	global TextOrSpeech

	#decide if input should be text or speech
	if TextOrSpeech == True:
		userInput = input(msg)
	else:
		#listen for microphone input
		with sr.Microphone() as source:
			audio = r.listen(source, phrase_time_limit=5)
			try:
				userInput = r.recognize_google(audio)
				debug(f"I heard: {userInput}")
			except:
				userInput = "Error 321" 
	debug(f"Input: {userInput}", "magenta")
	return userInput
	
#Output from the machine
def output(out):
	global TextOrSpeech

	#check if text ouput is false or true
	if TextOrSpeech == True:
		debug(str(out), "cyan")
	else:
		debug(str(out), "cyan")
		try:
			speech.speak(out, "en")
		except AssertionError:
			pass
		except:
			pass
	
#Cleares the input from words like "please" or "could you" or smth. idk (ClearInput)
def ClearInput(userInput):
	global wordListPath
	debug("ClearInput start", "yellow")
	
	#wörter welche vom eingabe string entfernt werden.
	with open(wordListPath) as file:
		for line in file:
			for word in line.split():
				if word in words:
					pass
				else:
					words.append(word)
	
	#wörter vom input entfernen
	userInput = userInput.lower()
	userInput = userInput.split()
	clearedInput = (' '.join([i for i in userInput if i not in words]))
	debug(f"Cleared input: {clearedInput}", "magenta")

	debug("ClearInput end")
	return clearedInput
	
#Check if call is a defined Programm and call it
def CheckAndCall(userInput):
	debug("CheckAndCall start", "yellow")
	
	#Clear the Input
	clearedInput = ClearInput(userInput)
	
	#Start to Check
	try: 
		switchedCall = switch[clearedInput]()
		debug("CheckAndCall end")
		return switchedCall
	except:
		debug("CheckAndCall end")
		return "Sorry i dont think i can help you with that."

#Error if voice is not recognizable		
def Error321():
	debug("Speech not understandable", "red")
		
#restarting to apply changes. just so you dont have to do it manually (cleares console)		
def restart():
	os.system("clear")
	output("Restarted Program")
	call()
	return "exitForRestart"

#---Applications---

#short for os.system
def com(command):
	os.system(command)

#say Hello
def TilihSaysHello(name = "user"):
	return f"Hello, {name}"

#open a new terminal
def OpenNewTerminal():
	com("gnome-terminal")
	return "Opening a new terminal."

#clearing the log
def clear():
	com("clear")
	return "Cleared the Log"

#calling the program after restart
def call():	
	print(colored("---Restarted Program---", "green" ))
	temporary = theUltimatePath + "Tilih.py"
	com("python3 "+ temporary)

#giving the last input
def tellLastInput():
	global lastInput
	if lastInput != False and lastInput != "None":
		return lastInput
	else:
		return "No saved last input."

#opening a command listen server
def comServer():
	com("gnome-terminal -x python3 "+comServerPath)
	return "Launching comServer"

#showing the command log
def tellComLog():
	global comLog
	global comLogPath

	comLog = []
	with open(comLogPath, "r") as file:
		for line in file:
			comLog.append(line)
	if comLog != False:
		comLogString = "".join(map(str, comLog))
		comLogString = str("\n----Log Start----\n" + comLogString + "\n----Log End----")
		return comLogString
	else:
		return "Nothing in the command log at the moment"

#write to the comlog. File as well as temporary
def writeToComLog(message):
	global comLog
	global comLogPath
	with open(comLogPath, "a") as file:
		file.write("\n")
		currentTime = str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		file.write(currentTime + " [+] " + message)
		comLog.append(message)
		file.close()

#clears the command log
def clearComLog():
	global comLogPath
	output("Are you sure you want to delete command log?")
	YesOrNo = Input()
	if "yes" in YesOrNo.lower() or "yeah" in YesOrNo.lower():
		with open(comLogPath, "w+") as file:
			file.write("")
		return "Command log was successfully deleted."
	elif "no" in YesOrNo.lower():
		return "Aboarding. Command log will not be deleted."

#append the list of words which will be removed from the input
def appendWordList():
	global wordListPath
	global words

	wordToAdd = Input("Word to append: ")
	if wordToAdd:
		if wordToAdd in words:
			return("This word is already in the word list.")
		else:	
			with open(wordListPath, "a") as file:
				file.write("\n")
				file.write(wordToAdd)
				file.close()
			return f"Added {wordToAdd} to the word list."
	else:
		debug("Something went wrong.", "red")

#remove a certain word from the word list
def removeWordFromList():
	global words
	global wordListPath

	wordToRemove = Input("Word to Remove: ")
	if wordToRemove:
		if wordToRemove in words:
			with open(wordListPath, "w+") as file:
				words.remove(wordToRemove)
				wordListString = "\n".join(map(str, words))
				file.write(wordListString)
				return f"Removed {wordToRemove} from the word list."
		else:
			return f"{wordToRemove} is not in the word list."
	else:
		return "The input was blank or wasnt recognized right."

#show the list of words which will be removed from the initial string. 
def showWordList():
	global words
	return words

#switching to text input
def switchToTextInput():
	global TextOrSpeech
	output("Do you really want to take input by text?")
	YesOrNo = Input()	
	if "yes" in YesOrNo.lower() or "yeah" in YesOrNo.lower():
		TextOrSpeech == True
		return "Switched to text input. Bye."
	elif "no" in YesOrNo.lower():
		return "Aboarding. Keeping voice input."
	
#switching to voice input
def switchToVoiceInput():
	global TextOrSpeech
	output("Do you really want to take input by speech?")
	YesOrNo = Input()	
	if "yes" in YesOrNo.lower() or "yeah" in YesOrNo.lower():
		TextOrSpeech == False
		return "Switched to voice input. Bye."
	elif "no" in YesOrNo.lower():
		return "Aboarding. Keeping text input."

#---------------------------------------------

#ALWAYS TYPE LOWER CASE COMMANDS!!!!!
switch = { 	
	#just say hi
	"hello" : TilihSaysHello,
	"hi" : TilihSaysHello,

	#open a new terminal
	"terminal" : OpenNewTerminal,
	"new terminal" : OpenNewTerminal,
	"open terminal" : OpenNewTerminal,

	#show the last given input
	"last input" : tellLastInput,
	"show last input" : tellLastInput,
	"tell last input" : tellLastInput,

	#command server for coms between phone and laptop
	"command server" : comServer,
	"start command server" : comServer,
	"launch command server" : comServer,
	"start comserver" : comServer,
	"launch comserver" : comServer,

	#command log from the current session
	"command log" : tellComLog,
	"comlog" : tellComLog,
	"show comlog" : tellComLog,
	"tell comlog" : tellComLog,
	"see comlog" : tellComLog,
	"show command log" : tellComLog,
	"tell command log" : tellComLog,
	"see command log" : tellComLog,

	#clears the command log
	"delete com log" : clearComLog,
	"delete command log" : clearComLog,
	"clear com log" : clearComLog,
	"clear command log" : clearComLog,

	#add another word to the word list
	"append word list" : appendWordList,
	"append words" : appendWordList,
	"add word to word list" : appendWordList,
	"add words to word list" : appendWordList,

	#remove a word from the word list
	"remove word" : removeWordFromList,
	"remove word from list" : removeWordFromList,
	"remove word from word list" : removeWordFromList,
	"remove words" : removeWordFromList,
	"remove word from words" : removeWordFromList,

	#show word list
	"show words" : showWordList,
	"see words" : showWordList,
	"see wordlist" : showWordList,
	"see word list" : showWordList,
	"show wordlist" : showWordList,
	"wordlist" : showWordList,

	#switch to text input
	"text input" : switchToTextInput,
	"switch text input" : switchToTextInput,
	
	#switch to voice input
	"voice input" : switchToVoiceInput,
	"switch voice input" : switchToVoiceInput,

	#system functions
	"error 321" : Error321,
	"clear" : clear,
	"restart" : restart,
}

#Show Debug? and text or speech?
ShowDebug()
TextOrSpeech()

#---Actual Script---

#introduction
output("Hey im Tilih. How may i help you?")

#input - output loop
while schleife:
	loopInput = Input()
	if loopInput.lower() == "exit":
		output("Bye, Bye.")
		schleife = False
		break
	else:
		CAC = CheckAndCall(loopInput)
		if CAC != "exitForRestart":	
			output(CAC)
			lastInput = loopInput
			if loopInput != "clear com log":
				writeToComLog(loopInput)
		else:
			schleife = False
