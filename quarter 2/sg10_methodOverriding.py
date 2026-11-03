class Animal:     #super class
    def __init__(self, name: str):
        self._name = name
    
    def eat(self):    #makes method for animal to eat
        print(self._name, "eats.")
        
    def make_sound(self):    #makes method for animal to make sound
        print(self._name, "makes a sound!")

#making another sub class under super class Animal
class Lion(Animal):     #subclass Lion from super class Animal
    def __init__(self, name: str):
       super().__init__(name)
    
    def eat(self):    #overrides super class eat function
        print(self._name, "eats fresh meat.")

    def make_sound(self):    #overrides super class make_sound function
        print(self._name, "roars loudly!")

#making another sub class under super class Animal
class Elephant(Animal):     #subclass Elephant from super class Animal
    def __init__(self,name: str):
        super().__init__(name)
    
    def eat(self):    #overrides super class eat function
        print(self._name, "eats grass and fruits.")

    def make_sound(self):    #overrides super class make_sound function
        print(self._name, "trumpets!")

#making another sub class under super class Animal
class Monkey(Animal):     #subclass Monkey from super class Animal
    def __init__(self,name: str):
        super().__init__(name)
    
    def eat(self):    #overrides super class eat function
        print(self._name, "eats bananas")

    def make_sound(self):    #overrides super class make_sound function
        print(self._name, "chatters!")


#program proper
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")

#main code was slightly modified from the given activity guide to achieve the desired output
