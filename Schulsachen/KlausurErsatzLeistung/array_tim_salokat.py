from termcolor import colored
#if your computer doesnt have this module installed run pip/pip3 install termcolor


datenbank = [
   ["PID", "Vorname", "Nachname", "Adresse", "PLZ", "Wohnort"],
   ["1", "Ali", "Uygun", "Wallstraße 25", "32839", "Steinheim"],
   ["2", "Bertha", "Meier", "Borkumstraße 54", "13189", "Berlin"],
   ["3", "Clara", "Friese", "Georgswall 3", "26603", "Aurich"],
   ["4", "Daniel", "Lehmann", "Komödienstieg 1", "22747", "Hamburg"],
   ["5", "Emma", "Malony", "Harburger Straße 47", "21614", "Buxtehude"]
]

#----just some quality of life. Ignore this----
def color(message):
    print("Running " + colored(message, "green"))
#----------------------------------------------

def taskOne():
    print(datenbank[2][2])

def taskTwo():
    for i in range(1, len(datenbank[1])):
        print(datenbank[0][i] + ": " + datenbank[1][i])

def taskThree():
    for i in range(1, len(datenbank)):

        if str(datenbank[i][2])[0] == "M":                                  #Check if the last name from the person starts with a capital M

            print("\n")                                                     #Seperate the data of different persons
            for n in range(1, len(datenbank[i])):
                
                print(datenbank[0][n] + ": " + datenbank[i][n])             #Print all of the persons data

def taskFour():

    Auswahl = input("Mit welchem Buchstaben beginnt der Nachname: ")
    Auswahl = Auswahl.capitalize()                                          #Capitalize the letter because the last name in the array always starts with a capital
    Ausgegeben = 0                                                          #Variable to count the printed out data

    for i in range(1, len(datenbank)):

        if str(datenbank[i][2])[0] == Auswahl:                              #Check if the last name from the person starts with the inputet letter
            
            Ausgegeben +=1
            print("\n")                                                     #Seperate the data of different persons
            for n in range(1, len(datenbank[i])):

                print(datenbank[0][n] + ": " + datenbank[i][n])             #Print all of the persons data

    if Ausgegeben == 0:
        print("Es tut mir leid doch im Verzeichnis ist niemand dessen Nachname mit " + Auswahl + " beginnt.")         

def taskFive():
    Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in range(0, len(Alphabet)):

        Auswahl = Alphabet[letter].capitalize()
        for i in range(1, len(datenbank)):

            if str(datenbank[i][2])[0] == Auswahl:                          #Check if the last name from the person starts with the inputet letter
                
                print("\n")                                                 #Seperate the data of different persons
                for n in range(1, len(datenbank[i])):

                    print(datenbank[0][n] + ": " + datenbank[i][n])         #Print all of the persons data

def taskSix():
    
    #DISCLAIMER: Everything inputed here will be saved to the global "datenbank" variable. So the information will be included in Task1-5 too.

    newRecord = []                                                          #Create a new record (Datensatz)
    newRecord.append(str(len(datenbank)))                                   #Set the number of the record
    newRecord.append(input("First name: "))
    newRecord.append(input("Last name: "))
    newRecord.append(input("Street and house number: "))                    #Input all the Information and add it to the new record
    newRecord.append(input("Postcode: "))
    newRecord.append(input("In which city do you live: "))
    
    datenbank.append(newRecord)                                             #Add the new Record to the "datenbank"
    print(datenbank)

#making you pick the code you want to run
def WählenDerAufgabe():
    
    while True:
        pickTask = input("Welche Aufgabe würden sie sich gerne ansehen? 'e' to exit (1-6): ")
        
        #Try converting the Input to an integer. 
        try:
            pickTask = int(pickTask)
        except:
            print("Bitte geben sie eine valide Zahl ein")
            #continue
            break
        
        #pick the answer and run the coresponding program
        try:
            if pickTask == 1:
                color("Aufgabe 1")
                taskOne()

            elif pickTask == 2:
                color("Aufgabe 2")
                taskTwo()

            elif pickTask == 3:
                color("Aufgabe 3")
                taskThree()

            elif pickTask == 4:
                color("Aufgabe 4")
                taskFour()

            elif pickTask == 5:
                color("Aufgabe 5")
                taskFive()
            
            elif pickTask == 6:
                color("Aufgabe 6")
                taskSix()

            else:
                print("Bitte geben sie eine valide Zahl ein")
            
            #Seperate new inputs a bit
            print("\n")

        except:
            print(colored("Hier ist irgendwas schief gegangen. Bitte versuchen sie es erneut.", "red"))      

WählenDerAufgabe()