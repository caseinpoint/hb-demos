class Hackbrighter:
    """A human at hackbright."""

    loves_python = True

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def introduce(self):
        print(f"Hi! My name is {self.name}. I'm a {self.title}")

class Student(Hackbrighter):
    pass