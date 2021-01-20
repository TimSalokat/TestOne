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
    recvMessage = connection.recv(1024)
    recvMessage = recvMessage.decode()
    print(client_name + ">" + recvMessage)
    
#to write and send messages
def writer():
    global sendMessage
    sendMessage = input(str("Me > "))
    #try:
    connection.send(sendMessage.encode())
    debug("Send")
    #except:
    #    debug("Couldnt send message", "red")

#---pre definition---

#stuff for the socket connection
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name,port))

#your diplayed name
yourName = input("Name to display: ")

#---cool code---

#wait for any connection, accept, show, get name from client
debug("waiting for incoming connections")
soc.listen(1)
connection, addr = soc.accept()
debug("connected with "+addr[0])
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + " has connected")

#Start writer and listener as soon as connection is established

Thread(listener()).start()
Thread(writer()).start()