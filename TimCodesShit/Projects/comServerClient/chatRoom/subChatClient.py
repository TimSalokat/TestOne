import time, os, socket, sys
from termcolor import colored
from threading import Thread

#only works on linux

#---defining funny stuff---

#void function
def void():
    return 0

#debug message in color
def debug(message = "debug", color = "green"):
    print(colored(message, color))

