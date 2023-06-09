class Cat:
    _data_file = 'cats.csv'
    greeting = 'Meow'
    species = 'cat'

    def __init__(self, name, hunger=100):
        self.name = name
        self.hunger = hunger

    def speak(self):
        print(f"{self.greeting}, I'm {self.name} the {self.species}!")

    def feed(self, calories):
        self.hunger = self.hunger - calories

    @staticmethod
    def food_to_calories(food_amt):
        """Convert an amount of cat food to calories."""

        return food_amt * 0.3456

    @classmethod
    def from_file(cls, name):
        """Create a cat using data from a file."""

        for line in open(cls._data_file):
            data_name, data_hunger = line.strip().split(',')

            if data_name == name:
                return cls(data_name, float(data_hunger))

    # @staticmethod
    # def from_file(name):
    #     """Create a cat using data from a file."""

    #     for line in open(Cat._data_file):
    #         data_name, data_hunger = line.strip().split(',')

    #         if data_name == name:
    #             return Cat(data_name, float(data_hunger))