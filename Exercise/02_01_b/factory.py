
class Dog:
    i = 0
    def __init__ (self):
        self.i += 1
        print("Dog created {}".format(self.i))

    def speak(self):
        return "Woof!"
    
dog1 = Dog()
print(dog1.speak())
dog2 = Dog()
print(dog2.speak())
dog3 = Dog()
print(dog3.speak())