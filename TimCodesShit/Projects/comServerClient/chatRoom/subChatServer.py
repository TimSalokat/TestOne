import time, os, socket, sys
from termcolor import colored
from threading import Thread

#only works on linux

#---defining funny stuff---

#void function
def void():
    return 0

#debug message in color
def debug(message = "debug", color = "green", fromFunction = "None"):
    fromFunction = str(fromFunction + ": ")
    print(colored(fromFunction, "cyan"), end="")
    print(colored(message, color))

def acceptConnection():
    global connected
    global host_name
    global soc
    global port
    global ip
    global connection
    global addr
    connected = False
    debug("Trying to establish a connection.", "yellow", "acceptConnection")
    try:
        soc = socket.socket()
        host_name = socket.gethostname()
        ip = socket.gethostbyname(host_name)
        port = 1234
        soc.bind((host_name, port))
        soc.listen(1)
        connection, addr = soc.accept()
        debug("Connected.", "green", "acceptConnection")
        connected = True
    except:
        connected = False
        debug("Could'nt connect to client.", "red", "acceptConnection")
    return connected

def iWannaWrite(connected):
    request = "CODE_WRITE"
    if connected == True:
        #mach halt weider
        debug("Connected.", "green" ,"iWannaWrite")
        debug("Sending writing request.", "yellow", "iWannaWrite")
        soc.send(request.encode())
        debug("Request send.", "green", "iWannaWrite")
    else:
        try:
            debug("Starting acceptConnection.", "yellow", "iWannaWrite")
            acceptConnection()
            debug("Connected", "green", "iWannaWrite")
            debug("Sending writing request.", "yellow", "iWannaWrite")
            soc.send(request.encode())
            debug("Request send.", "green", "iWannaWrite")
        except:
            debug("Could'nt connect to client.", "red", "iWannaWrite")