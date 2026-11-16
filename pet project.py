from idlelib.sidebar import WrappedLineHeightChangeDelegator
from shutil import which


class pet:
    def __init__(self, name, species, hunger, happiness):
        self.name = name #variables to save self as a local variable
        self.species = species
        self.hunger = self.hunger
        self.happiness = happiness

        if happiness > 100: #loop to set happiness to 100 if it exceeds cap
            self.happiness = 100
        if happiness < 0: #loop to set happiness to 0 if it exceeds cap
            self.happiness = 0
        if hunger > 100: #loop to set hunger to 100 if it exceeds cap
            self.hunger = 100
        if hunger < 0: #loop to set hunger to 0 if it exceeds cap
            self.hunger = 0
    def feed(self):
        self.hunger = self.hunger + 20
    def play(self):
        self.happiness = self.happiness + 20
        self.hunger = self.hunger - 20
    def sleep(self):
        self.happiness = 100
    def display_status(self):
        print(self.name)
        print(self.species)
        print("hunger" + self.hunger)
        print("happiness" + self.happiness)

pet1 = pet("benji", "cat", 20, 100)
pet2 = pet("ferry", "fox", 20, 20)

while True:
    pet1.display_status()
    print("------------------------------")
    pet2.display_status()
    print("------------------------------")
    WhichPet = input("Which pet would you like to interact with?: ").lower()

    if WhichPet == "benji":
        print("1. Display stats")
        print("2. Feed")
        print("3. Sleep")

        wwyd = input("What would you like to do? ")

        match wwyd:
            case "1":
                pet1.display_status()
            case "2":
                pet1.feed()
            case "3":
                pet1.sleep()

    elif WhichPet == "ferry":
        print("1. Display stats")
        print("2. Feed")
        print("3. Sleep")

        wwyd = input("What would you like to do? ")

        match wwyd:
            case "1":
                pet2.display_status()
            case "2":
                pet2.feed()
            case "3":
                pet2.sleep()

    else:
        print("Pet not found!")