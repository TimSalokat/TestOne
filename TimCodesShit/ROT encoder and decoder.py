#
#These are comments with my TODO
#Program which takes text input and then uses all or just one ROT encryption and prints it out.
#if in the encoded text is a word like "der die das" or smth. mark it green or red idk. which color.
#

from termcolor import colored
import os, sys
os.system("cls")

#color
def color(message, color = "green"):
    print(colored(message, color))

#encrypting funtion
def encrypt():

    #inputing the ROT number and the message to be encryptet
    rotNumber = input("Which 'ROT' do you want to encrypt 1-26: ")
    message = input("Message you want to encrypt: ")
    message = message.lower()
    ABC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #check which number to use
    if int(rotNumber) in range(1, 27):
        newMessage = []
        rotNumber = int(rotNumber)
        letter = 0
        while letter <= int(len(message) - 1):

            #find letter in abc
            letternumber = 0
            if message[letter] != " ":
                while ABC[letternumber] != message[letter]:
                    if letternumber <=25:
                        letternumber += 1
                    elif letternumber == 26:
                        letternumber = 0
            
                #change letter to right thing
                if letternumber + rotNumber in range(1, 27):
                    if letternumber + rotNumber == 26:
                        letternumber = 0
                        newMessage.append(ABC[letternumber])
                    else:
                        newMessage.append(ABC[letternumber + rotNumber])
                else:
                    newMessage.append(ABC[letternumber + rotNumber - 26]) 
            else:
                newMessage.append(" ")
            letter += 1
        message = "".join(newMessage)
        print(message)
    else: 
        print("Please input again")
        encrypt()

#encrypting funtion
def decrypt(rotNumber = "", message = ""):

    #inputing the ROT number and the message to be encryptet
    if rotNumber == "":
        rotNumber = input("Which 'ROT' do you want to encrypt 1-26 or all: ")
    if message == "":
        message = input("Message you want to encrypt: ")
    message = message.lower()
    ABC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    keywords = ["der", "die", "das", "the", "ich", "du", "er", "sie", "es"]

    #check which number to use
    if rotNumber == "all":
        x = 0
        for x in range(1,27):
            color(x, "blue")
            decrypt(x, message)
            print("-" * 20)
            x += 1
    elif int(rotNumber) in range(1, 27):
        newMessage = []
        rotNumber = int(rotNumber)
        letter = 0
        while letter <= int(len(message) - 1):

            #find letter in abc
            letternumber = 0
            if message[letter] != " ":
                while ABC[letternumber] != message[letter]:
                    if letternumber <=25:
                        letternumber += 1
                    elif letternumber == 26:
                        letternumber = 0

                #change letter to right thing
                if letternumber - rotNumber in range(0, 26):
                    newMessage.append(ABC[letternumber - rotNumber])
                elif letternumber - rotNumber < 0:
                    newMessage.append(ABC[letternumber - rotNumber + 26])
            else:
                newMessage.append(" ")
            letter += 1
        message = "".join(newMessage)
        temporary = False
        wordlist = message.split()
        for word in wordlist:
            for keyword in keywords:
                if word == keyword:
                    color(message, "green")
                    temporary = True
                    break

        if temporary != True:
            print(message)
    else: 
        print("Please input again")
        decrypt()

def code():
    temporary = input("Do you want to encrypt or decrypt? e/d/exit: ")
    if temporary == "e":
        encrypt()
        code()
    elif temporary == "d":
        decrypt()
        code()
    elif temporary == "exit":
        pass
    else:
        code()

#---actual code---
code()