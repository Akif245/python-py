class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("Sound by animal")
class dog(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name, species="DOG")
        self.breed=breed
    def makesound(self):
        print("Bark!")
A=dog("DOGGY","DOGGERMAN")
A.makesound()
B=Animal("CAT","CITTY")
B.makesound()
        