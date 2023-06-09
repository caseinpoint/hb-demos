# crenshaw = {
#     "price": 2.00,
#     "color": "green",
#     "source": ["USA", "Brazil"],
#     "seedless": False,
# }
# watermelon = {
#     "price": 3.00,
#     "size": "large",
#     "comes_from": ["USA", "Spain"],
# }

# def buy_melon(melon_type):
#     """Buy a melon, checking source country and price."""
#     print(f'You bought a melon from {melon_type["source"]} for ${melon_type["price"]}.')

print(__name__)


class Cat:
    """A cat. Felis catus"""

    species = 'cat'

    def __init__(self, name, color):
        self.name = name.title()
        self.color = color

    def __repr__(self):
        return f'<Cat name={self.name}>'

    def speak(self):
        print(f'Meow! I am {self.name} the {self.species}.')

    def rename(self, new_name):
        self.name = new_name

    def dance(self, times=3):
        return ':prance:' * times

    def graduate(self):
        self.name = 'Dr. ' + self.name
        self.speak()
        # self.name = f'Dr. {self.name}'


if __name__ == '__main__':
    felix = Cat('felix', 'tuxedo')

    kitty = Cat('KITTY', 'tabby')
