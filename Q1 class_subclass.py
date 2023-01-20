class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
    def __str__(self) -> str:
        ans = "I am a " + self.species + " named " + self.name
        return ans
    def make_sound(self):
        pass

class Cow(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, species="cow")
    def make_sound(self):
        return "Moow"

class Horse(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, species="neigh")
    def make_sound(self):
        return "Neigh"
    
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, species="")
    def make_sound(self):
        return "Woof"
# cow1 is an object of Animal class, so it has __str__ but make_sound is not implemented
cow1 = Animal("Binni", "cow")
print(cow1)
print(cow1.make_sound()) #Prints None
# cow2 is an object of Cow class, it can make sound
cow2 = Cow("Jany")
print(cow2)
print(cow2.make_sound()) #Prints Moow