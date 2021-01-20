import time, socket, os, sys
from termcolor import colored
from threading import Thread

#---defining funny stuff---

#void function
def void():
    return 0

#debug message in color
def debug(message = "debug", color = "green"):
    print(colored(message, color))

#listen for messages
def listener():
    global recvMessage
    recvMessage = soc.recv(1024)
    recvMessage = recvMessage.decode()
    print(server_name + ">" + recvMessage)

#to write and send messages
def writer():
    global sendMessage
    sendMessage = input(str("Me > "))
    #try:
    soc.send(sendMessage.encode())
    debug("Send")
    #except:
    #    debug("Couldnt send message", "red")

#---pre definition---

#stuff for socket connection
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
server_host = input("Server IP: ")
port = (int(input("Server PORT: ")))
name = input("Name to display: ")

#---cool code---

#connect to server with given information
soc.connect((server_host, port))
debug("Connecting to server")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
debug("Connected")

#start listener and writer

Thread(writer()).start()
Thread(listener()).start()