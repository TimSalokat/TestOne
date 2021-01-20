import sys, os, socket, time
from termcolor import colored

#only works on linux

#---dedicated Client version---
dedicatedClientVersion = 1.208
#---defining stuff/variables---
#TODO Server
#Editing Files
#reset comline on client disconnect
#
#Autoconnect to ngrok?
#Receiving Files
#connect to tilih
#failsave?
#windows pc
#server shell
#new lineS for ls etc. 
#
#
#TODO Client
#recv file error on : sorry i dont know this command
#close the connection on client error
#dont just override files
#on couldnt connect retry with own input of condetails
#

theUltimatePath = "/home/parrot/Documents/Python/Projects/comServerClient/commandsPhoneLaptop/"

soc = socket.socket()
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
com_line = False
Exit = False

#making the output file but in shit

#getting the current path
os.system("touch temp.txt")
file = open ("temp.txt", "r+")
os.system("pwd >> temp.txt")
path = str(file.readlines(0))
path = path.replace("n']", "").replace("['", '').replace("\\", "")
path2 = str(path + "/output.txt")
file.close()
os.system("rm -r -f temp.txt")

#start ngrok
temporary = str(f"gnome-terminal -x python3 {theUltimatePath}ngrok0.py &")
os.system(temporary)

#deleting and initializing output path
try:
    os.chdir(path)
    os.system("rm -r -f output.txt")
    os.system("touch ", path2)
    file = open(path2, "r+")
except:
    command = "touch " + path2
    os.system(command)
    file = open(path2, "r+")

#---defining funtions---

#void function
def void(returning = 0):
    return returning

#print in easier and colored
def debug(message = "debug", fromFunction = "Temporary", color = "green", whichDebug = "main"):
    sideDebug = "OFF"
    if whichDebug == "side" and sideDebug == "OFF" and color != "red":
        void()
    else:
        fromFunction = str(fromFunction + ": ")
        print(colored(fromFunction, "cyan"), colored(message, color))

#something shorter than os.system()
def com(command):
    global file
    global com_line
    debug("Com started", "Com", "yellow", "side")

    #check if command is cd and if not run the normal command
    if command[0] + command[1] != "cd":
        try:
            command = command + ">> " + path2
            os.system(command)
            returnDing = file.readlines()
        except:
            debug("Command not found", "Com", "red")
    elif command == "ext comline":
        com_line = False
        returnDing = "Exiting comline"
    else:
        command = command.split()
        try:
            os.chdir(command[1])
            returnDing = file.readlines()
        except:
            debug("Something went wrong", "Com", "red")

    if returnDing:
        debug("Com finished", "Com", "green", "side")
        return returnDing
    else:
        returnDing = "This command has no return"
        debug("Com finished", "Com", "green", "side")
        return returnDing

#interpreter which recognizes the command
def interpreter(command):
    global com_line
    try:

        #make input lower case
        debug("Interpreter started", "Interpreter", "yellow", "side")

        #check command is for command line
        if command.lower() == "comline" and com_line == False:
            com_line = True
            returningMessage = "Command line activated."
            debug("Comline activated", "Interpreter")
        elif command.lower() == "comline" and com_line == True:
            returningMessage = "Command line is already active."
        else:

            #send command to terminal
            if "edit " in command.lower() and com_line == True:
                temporary = command.replace("edit ", "")
                #try:
                writer("Sending File") #THATS IMPORTANT
                temporary = os.getcwd().replace("/ ", "/") + "/" + temporary
                debug(f"Sending {temporary}", "Interpreter:Edit", "yellow", "side")
                sendFile(temporary)
                returningMessage = "No Return"
                #except:
                #    debug("Error sending the file.", "Interpreter:Edit", "red")
                #    returningMessage = "Couldnt find the file you were looking for."

            elif com_line == True and command.lower() != "bye" and command.lower() != "ext comline":
                returningMessage = com(command)

            #if message is ext comline close the command line program
            elif com_line == True and command.lower() == "ext comline" and command.lower() != "bye":
                com_line = False
                returningMessage = "Exiting command line"

            #if commandline is false check for normal commands
            else:
                command = command.lower()
                if command == "hello" or command == "hi":
                    returningMessage = "Hey"
                elif command == "bye":
                    returningMessage = "bye"
                elif command == "fuck you":
                    returningMessage = "No u!"
                elif command == "how are you?":
                    returningMessage = "Fine you?"
                elif command == "help":
                    returningMessage = "You moron didnt add a help list yet."
                
                #if nothing is regognizable
                else: 
                    returningMessage = "Couldnt regocnize anything so fuck you"

        #check if returningMessage has content and if not give it some
        if returningMessage and returningMessage != "No Return":
            debug("Interpreter finished", "Interpreter", "green", "side")
            return returningMessage
        elif returningMessage == "No Return":
            return 0
        else:
            returningMessage = "Something went wrong."
            debug("Interpreter finished", "Interpreter", "green", "side")
            return returningMessage

    #if something goes wrong this happens
    except:
        returningMessage = "Sorry i dont know this command"
        debug("Interpreter finished", "Interpreter", "green", "side")
        return returningMessage

#the writer
def writer(message):
    debug("Started writer", "Writer", "yellow", "side")
    debug(f"{message}", "Writer", "magenta")
    if message and message != 0:
        message = str(message)
        try:
            connection.send(message.encode())
            debug("Writer finished", "Writer", "green", "side")
        except BrokenPipeError:
            debug("Broken Pipe", "General", "red")
            connect()
        except:
            debug("Something went fucking wrong", "Writer", "red")
    elif message == 0:
        void()
    else:
        debug(f"Couldnt send {message}", "Writer", "red")

#the message listener
def listener(interpret = True):
    debug("Started listener", "Listener", "yellow", "side")
    global message
    message = connection.recv(1024)
    message = str(message.decode())
    debug(f"{message}", "Listener", "magenta")
    if interpret == True:
        message = interpreter(message)
        if message == "bye":
            return "bye"
        else:
            writer(message)
    debug("Listener finished", "Listener", "green", "side")

#send a certain file to the client
def sendFile(filepath):
    time.sleep(1.5)
    with open(filepath, "rb") as f:
        debug("Sending File", "SendFile")
        debug(f"Sending file with name {filepath}", "SendFile", "yellow", "side")
        while True:
            toSend = f.read(50)
            if toSend:
                connection.send(toSend)
            else:
                break
    debug(f"Send {filepath} sucessfully.", "SendFile", "green", "side")
    debug("Finished sending the file.", "SendFile")

#check the version of the Client and if necessary send the new code
def versionCheck():
    global dedicatedClientVersion
    global theUltimatePath

    #send dedicated client version
    clientVersion = connection.recv(1024)
    clientVersion = clientVersion.decode() 

    #sending the dedicated version
    dedicatedClientVersion = str(dedicatedClientVersion)
    connection.send(dedicatedClientVersion.encode())

    #check the versions and send new one if needed
    if clientVersion != dedicatedClientVersion:
        debug("Client version is false. Sending right code.", "VersionCheck", "red")
        #try:
        temporary = str(f"{theUltimatePath}comClientNew.py")
        sendFile(temporary)
        return False
        #except:
        #    debug("An error occured while sending the right version.", "VersionCheck", "red")
        #    return False
    else:
        debug("Finished version check.", "VersionCheck", "green", "side")
        return True

#Connect, handshake, versionCheck and writer/listener
def connect():
    global connection
    debug("Waiting for incoming connection.", "Connect", "yellow")
    soc.listen(1)
    connection, addr = soc.accept()
    
    #recieve handshake
    package = connection.recv(1024)
    debug("package received", "Handshake", "green")
    package = package.decode()

    #send handshake
    returnPackage = "hemtcp"
    connection.send(returnPackage.encode())
    debug("package send", "Handshake", "green")

    #check received package and establish connection
    if package == "pctmeh":
        debug("Connected to " + addr[0], "Connect")
        if versionCheck() == True:
            while True:
                if listener() == "bye":
                    writer("bye")
                    debug("Client Exiting", "Connect")
                    Exit = True
                    break
                else:
                    void()
        else:
            debug("Client Version is false. Restarting client.", "Connect", "red")
            connect()
    else:
        debug("There was a problem with the package switch.", "None", "red")
        connect()

def editFile(Filename):
    void()

#---actual code---

try:
    if Exit == False:
        connect()
    else:
        void()
except KeyboardInterrupt:
    debug("Exiting", "Actual Code", "magenta")
    void()
except: 
    if Exit == False:
        debug("An Error occured.", "Connect", "red")
        connect()
    else:
        void()