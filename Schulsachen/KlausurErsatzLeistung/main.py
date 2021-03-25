from termcolor import colored

global datenbank
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

def One():
    print(datenbank[2][2])

def Two():
    for i in range(1, len(datenbank[1])):
        print(datenbank[0][i] + ": " + datenbank[1][i])

def Three():
    for i in range(1, len(datenbank)):

        if str(datenbank[i][2])[0] == "M":                                  #Check if the last name from the person starts with a capital M

            print("\n")                                                     #Seperate the data of different persons
            for n in range(1, len(datenbank[i])):
                
                print(datenbank[0][n] + ": " + datenbank[i][n])             #Print all of the persons data

def Four():

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

def Five():
    Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in range(0, len(Alphabet)):

        Auswahl = Alphabet[letter].capitalize()
        for i in range(1, len(datenbank)):

            if str(datenbank[i][2])[0] == Auswahl:                          #Check if the last name from the person starts with the inputet letter
                
                print("\n")                                                 #Seperate the data of different persons
                for n in range(1, len(datenbank[i])):

                    print(datenbank[0][n] + ": " + datenbank[i][n])         #Print all of the persons data

#making you pick the code you want to run
def AufgabeWählen():
    
    while True:
        Auswahl = input("Welche Aufgabe würden sie sich gerne ansehen? (1-9): ")
        
        #Try converting the Input to an integer. 
        try:
            Auswahl = int(Auswahl)
        except:
            print("Bitte geben sie eine valide Zahl ein")
            #continue
            break
        
        #pick the answer and run the coresponding program
        try:
            if Auswahl == 1:
                color("Aufgabe 1")
                One()
                print("\n")

            elif Auswahl == 2:
                color("Aufgabe 2")
                Two()
                print("\n")

            elif Auswahl == 3:
                color("Aufgabe 3")
                Three()
                print("\n")

            elif Auswahl == 4:
                color("Aufgabe 4")
                Four()
                print("\n")

            elif Auswahl == 5:
                color("Aufgabe 5")
                Five()
                print("\n")

            else:
                print("Bitte geben sie eine valide Zahl ein")
        except:
            print(colored("Sorry something went wrong. Exiting", "red"))      

AufgabeWählen()