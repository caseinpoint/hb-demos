class Hackbrighter:
    """A person at Hackbright."""

    hours_per_week = 40

    def __init__(self, name, title, pronouns="unspecified"):
        self.name = name
        self.title = title
        self.pronouns = pronouns
        self.diet = diet

    def introduce(self):
        print(f"Hi! My name is {self.name}. My pronouns are {self.pronouns}.")

class Student(Hackbrighter):
    """A student at Hackbright."""

    has_lightning_talk = True
    hours_per_week = 50

    def __init__(self, name, pronouns="unspecified"):
        super().__init__(name, "student", pronouns)
        self.grades = {}

    def introduce(self):
        super().introduce()
        print(f"I'm an excellent {self.title} at Hackbright.")

    def add_grade(self, assignment, score):
        pass
