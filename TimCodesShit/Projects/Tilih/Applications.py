#!/bin/python3

import os
from termcolor import colored

def com(command):
	os.system(command)
	

def TilihSaysHello():
	return "hello, you"
def OpenNewTerminal():
	com("gnome-terminal")
	return "opening new terminal"
def clear():
	com("clear")
	return "Cleared the Log"
def call():	
	print(colored("---Restarted Program---", "green" ))
	com("python3 /home/kali/Documents/Python/Tilih/Tilih.py")
def tellLastInput():
	return 0
