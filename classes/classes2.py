class Animal:
    max_hunger = 50

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self, greeting="Hey"):
        return f"{greeting}, My name is {self.name}, and I am a(n) {self.species}!"


class Cat(Animal):
    max_purr_vol = 10
    max_hunger = 70

    def __init__(self, name, purr_vol):
        super().__init__(name, "cat")
        self.purr_vol = purr_vol

    def speak(self):
        return super().speak("Meow")


class FriendlyCat(Cat):
    def speak(self):
        msg = super().speak()
        return f"{msg} You seem awesome."


# if __name__ == '__main__':
    # felix = Cat('Felix', 'dog')
    # # print('felix', id(felix))
    # print(felix.species)
    # # felix.speak()
    # # felix.graduate()

    # felix = Animal('Felix', 'cat')
    # fido = Animal('Fido', 'dog')

    # felix.speak()
    # fido.speak()

class Tire:
    max_rim_size = 100
    def __init__(self, size, material):
        pass


class Car:
    def __init__(self):
        self.tires = [Tire(), Tire(), Tire(), Tire()]