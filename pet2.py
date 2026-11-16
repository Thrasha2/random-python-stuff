
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def clamp_stat(self, stat):
        return max(0, min(100, stat))

    def clamp_all_stats(self):
        self.hunger = self.clamp_stat(self.hunger)
        self.happiness = self.clamp_stat(self.happiness)
        self.energy = self.clamp_stat(self.energy)

    def feed(self):
        self.hunger -= 15
        self.happiness += 5
        self.clamp_all_stats()

    def play(self):
        self.hunger += 10
        self.happiness += 15
        self.energy -= 20
        self.clamp_all_stats()

    def sleep(self):
        self.energy += 30
        self.clamp_all_stats()

    def display_status(self):
        print("Name:", self.name)
        print("Hunger:", self.hunger)
        print("Happiness:", self.happiness)
        print("Energy:", self.energy)


pet = Pet("Benji")

running = True
while running:
    print("---Pet Sim---")
    print("1. Display stats")
    print("2. Feed")
    print("3. Play")
    print("4. Sleep")
    print("5. Quit")

    choice=input("Enter your choice:")

    match choice:
        case "1":
            pet.display_status()
        case "2":
            pet.feed()
        case "3":
            pet.play()
        case "4":
            pet.sleep()
        case "5":
            running = False
            print("thanks for playing!")

pet.display_status()
