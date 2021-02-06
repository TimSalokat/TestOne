

#NOT WORKING

class Schüler:
    def __init__(self):
        self.name = input("What is his name: ")
        self.nonoPeopleCount = int(input(f"How many nono people has {self.name}: "))
        self.nonoGuy = []
        for i in range(0, self.nonoPeopleCount):
            self.nonoGuy.append(input(f"{i + 1} nono guy: "))
            i += 1

schülerNames = []
schüler = []
for i in range(0, input("Anzahl Schüler: ")):
    schülerNames.append(input(f"{i+1}'s schülers name: "))
    schüler.append((schülerNames[i] = Schüler()))

for i in range(0, len(schülerNames)):
    print(f"{schüler[i].name} has {schüler[i].nonoPeopleCount} nono people.")
    for x in range(0, schüler[i].nonoPeopleCount):
        print(f"{schüler[i].name}'s nono guy number {x + 1} is {schüler[i].nonoGuy[x]} ")


    