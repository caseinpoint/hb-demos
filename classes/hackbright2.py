class Hackbrighter:
    """A person at Hackbright."""

    hours_per_week = 40

    def __init__(self, name, title, pronouns="unspecified"):
        self.name = name
        self.title = title
        self.pronouns = pronouns

    def introduce(self):
        print(f"Hi! My name is {self.name}. My pronouns are {self.pronouns}.")

        if self.title[0].lower() in "aeiou":
            print(f"I'm an {self.title} at Hackbright.")
        else:
            print(f"I'm a {self.title} at Hackbright.")




































# class Student(Hackbrighter):
#     pass
