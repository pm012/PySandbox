'''
Define a SheepDog's subclass named LowlandDog, and equip it with an __str__() method overriding an inherited method of the same name. 
The new dog's __str__() method should return the string "Woof! I don't like mountains!".
'''

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"
    
class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + " I don't like mountins!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
lucky = LowlandDog("Shepperd")

print(rocky)
print(luna)
print(lucky)

