class AbstractAnimal:
    greeting = 'Hey'
    species = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Animal name={self.name}>'

    def speak(self):
        print(f"{self.greeting}, I'm {self.name} the {self.species}")


class ChaseLaserMixin:
    """Can chase laser pointers."""

    def chase_laser(self):
        print('Wheee!')


class HasFurMixin:
    """Has fur."""

    def enfur(self):
        print('Fur everywhere!!')


class Cat(ChaseLaserMixin, HasFurMixin, AbstractAnimal):
    greeting = 'Meow'
    species = 'cat'

    # def __init__(self, name):
    #     super().__init__(name)

    # def speak(self):
    #     super().speak("Meow")


class Dog(HasFurMixin, AbstractAnimal):
    greeting = 'Woof'
    species = 'dog'

    # def __init__(self, name):
    #     super().__init__(name)

    # def speak(self):
    #     super().speak("Woof")


class AnimalShelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_animal_names(self):
        for animal in self.animals:
            print(animal.name)

    def get_animals_by_species(self, species):
        animals_of_species = []

        for animal in self.animals:
            if animal.species == species:
                animals_of_species.append(animal)

        return animals_of_species

if __name__ == '__main__':
    felix = Cat('Felix')
    rover = Dog('Rover')

    my_shelter = AnimalShelter()
    my_shelter.add_animal(felix)
    my_shelter.add_animal(rover)