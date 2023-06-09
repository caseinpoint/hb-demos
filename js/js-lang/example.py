class Cat:
    def speak(self):
        return f'Meow!  I am {self.name} the cat!'
    
    @staticmethod
    def cat_food_to_calories(amt):
        return amt * .123

cat1 = Cat()
cat1.speak()

Cat.cat_food_to_calories(100)
