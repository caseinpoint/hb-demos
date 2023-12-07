crenshaw = {
    "price": 2.00,
    "color": "green",
    "source": ["USA", "Brazil"],
    "seedless": False,
}

def buy_melon(melon_type):
    """Buy a melon, checking source country and price."""

    print(f'You bought a melon from {melon_type["source"]} for ${melon_type["price"]}.')

buy_melon(crenshaw)

# watermelon = {
#     "price": 3.00,
#     "size": "large",
#     "comes_from": ["USA", "Spain"],
# }
# buy_melon(watermelon)





# class Cat:
#     """A cat."""

#     species = 'cat'
#     diet = 'carnivore'
#     fav_foods = ['kibble', 'canned tuna']

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f'<Cat object name={self.name}>'

#     def speak(self):
#         print(f'Meow! I am {self.name} the {self.species}')

#     def id_check(self, check):
#         print('id(self)=', id(self), 'check=', check)

#     def dance(self):
#         return ':prance, prance, prance:'

#     def graduate(self):
#         self.name = f'Dr. {self.name}'
#         self.speak()

# felix = Cat()
# felix.name = 'Felix'
# check = id(felix)
# felix.id_check(check)
# kitty = Cat()
# kitty.name = 'Kitty'


# def make_cat():
#     cat_instance = Cat()
#     return cat_instance
