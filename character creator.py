class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class

        if character_class == "worrior":
            self.health = 150
            self.mana = 100
        elif character_class == "mage":
            self.health = 100
            self.mana = 250
        elif character_class == "archer":
            self.health = 100
            self.mana = 100
    def DisplayStats(self):
        print(self.name)
        print(self.character_class)
        print(self.health)
        print(self.mana)
        print("----------------------")

player1 = Character("thrasha", "worrior")
player2 = Character("agorin", "archer")
player3 = Character("dante", "mage")

player1.DisplayStats()
player2.DisplayStats()
player3.DisplayStats()