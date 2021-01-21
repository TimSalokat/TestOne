import os
import socket
from termcolor import colored

#only works on android. Iguess?

#---Current Client version---
version = 1.208
#---defining stuff---
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

#deleting and initializing detail path
try:
    os.system("touch condetails.txt")
    file = open("condetails.txt", "r+")
except:
    file = open("condetails.txt", "r+")

#a void function aka return
def void(returning = 0):
    return returning

#debug function (just print in colored and fancy)
def debug(message = "debug", inFunction = "Dingens", color = "green"):
    inFunction = str(inFunction + ": ")
    print(colored(inFunction, "cyan"), colored(message, color))

#automatic connection
def autoconnect():
    global server_host
    global port
    with open("condetails.txt", "r"):
        server_host = str(file.readlines(1)).replace("n']", "").replace("['", '').replace("\\", "") + ".tcp.ngrok.io"
        port = str(file.readlines(2)).replace("n']", "").replace("['", '').replace("\\", "")
        port = int(port)
        debug(f"Connecting to {server_host}:{port}", "Autoconnect", "yellow")
        file.close()
    soc.connect((server_host, port))

#define port and host
def connect(tryAutoconnect = True):
    try:
        if tryAutoconnect == True:
            autoconnect()
        else:
            try:
                debug("Connection Failed. Please input manually.")
                os.system("rm -r -f condetails.txt")
                server_host = input(str("Server number: "))
                os.system("echo " + str(server_host) + " >> condetails.txt")
                server_host = server_host + ".tcp.ngrok.io"
                port = int(input("Server port: "))
                os.system("echo " + str(port) + " >> condetails.txt") 
            except:
                debug("Connection Failed. Please input manually.")
                server_host = input(str("Server number: "))
                os.system("echo " + str(server_host) + " >> condetails.txt")
                server_host = server_host + ".tcp.ngrok.io"
                port = int(input("Server port: "))
                os.system("echo " + str(port) + " >> condetails.txt") 
        debug(f"Connecting to {server_host}:{port}", "Connect", "yellow")
        soc.connect((server_host, port))
        debug("Connected.")
    except:
        try:
            debug("Connection Failed. Please input manually.")
            os.system("rm -r -f condetails.txt")
            server_host = input(str("Server number: "))
            os.system("echo " + str(server_host) + " >> condetails.txt")
            server_host = server_host + ".tcp.ngrok.io"
            port = int(input("Server port: "))
            os.system("echo " + str(port) + " >> condetails.txt") 
        except:
            debug("Connection Failed. Please input manually.")
            server_host = input(str("Server number: "))
            os.system("echo " + str(server_host) + " >> condetails.txt")
            server_host = server_host + ".tcp.ngrok.io"
            port = int(input("Server port: "))
            os.system("echo " + str(port) + " >> condetails.txt") 
        debug(f"Connecting to {server_host}:{port}", "Connect", "yellow")
        soc.connect((server_host, port))
        debug("Connected.")
#------

#listener
def listener():
    global message
    message = soc.recv(1024)
    message = message.decode()
    print(colored("Server: ", "blue"), message)
    return message

#writer
def writer(inFunction = False, message = "NULL"):
    if inFunction == False:
        try:
            message = str(input(colored("You: ", "cyan")))
            soc.send(message.encode())
        except KeyboardInterrupt:
            debug("Keyboard Interrupt. Aboarding", "writer", "red")
            message = "bye"
            soc.send(message.encode())
    else:
        message = str(message)
        soc.send(message.encode())
    return message

#receiving a given file
def recvFile(newFilename = "NULL"):

    if newFilename != "NULL":
        filename = newFilename
    try:
        os.system(f"touch {filename}")
    except:
        debug(f"Couldnt create {filename}, most likely file exists already.", "recvFile", "red")

    with open(filename, "wb") as f:
        temporary = "File doesnt exist"
        debug("Receiving file.", "RecvFile", "yellow")
        received = soc.recv(512)
        while True:
            if received:
                if received != "Sorry i dont know this command":
                    temporary = "None"
                    print(received)
                    f.write(received)
                    try:
                        soc.settimeout(5.0)
                        received = soc.recv(512)
                        soc.settimeout(None)
                    except:
                        break
                else:
                    temporary = "File doesnt exist"
                    break
            else:
                break
    if temporary != "File doesnt exist":
        debug(f"Sucessfully received {filename}.", "RecvFile")
    else:
        debug(f"{filename} doesnt exist.", "RecvFile")

#checking the version from the Client and if necessary changing it.
def versionSwitch(version):
    global soc
    global file

    #sending the version
    version = str(version)
    soc.send(version.encode())

    #receiving the right version
    dedicatedVersion = soc.recv(1024)
    dedicatedVersion = dedicatedVersion.decode()

    #check if dedicatedVersion is same as send version
    if dedicatedVersion != version:
        debug(str(version), "VersionCheck", "red")
        recvFile("comClientNew.py")
        debug("Finished receiving the new client file.", "VersionSwitch")
        os.system("mv comClient.py oldComClient.py")
        os.system("mv comClientNew.py comClient.py")
        debug("Finished renaming. Exiting versionSwitch", "VersionSwitch")
        return False
    else:
        debug(version, "VersionCheck")

        #if there is an old client version delete it.
        try:
            os.system("rm -f oldComClient.py")
        except:
            void()
        return True


#---funny actual code---

connect()

#send package
returnPackage = "pctmeh"
soc.send(returnPackage.encode())

#receive handshake from server
package = soc.recv(1024)
package = package.decode()
debug(package, "handshake", "green")

#check received packages and establish connection
if package == "hemtcp":
    if versionSwitch(version) == True:
        debug("Connected", "None")
        while True:
            sendMessage = writer()
            temporary = listener()

            if temporary == "bye":
                debug("Exiting program", "Exit")
                break
            elif temporary == "Sending File":
                sendMessage = sendMessage.lower().replace("edit ", "")
                recvFile(sendMessage)
            else:
                void()
    else:
        debug("Version check is false. Program will exit automatically, as soon as it does please start it again.", "Connect", "red")
else:
    connect()
    debug("Couldnt connect to server.", "None", "red")