class Dog():
    def __init__(self,  name):
        self.name = name
    def speak(self):
        return self.name + ' say woof'

class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' say meow'

if __name__ == '__main__':
    niko = Dog("niko")
    felix = Cat('felix')
    for pet in [niko, felix]:
        print(pet.speak())
