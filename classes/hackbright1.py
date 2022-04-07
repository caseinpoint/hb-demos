class HackbrightStudent:
    """A student at Hackbright."""

    hours_per_week = 40

    def __init__(self, student_name, pronouns="unspecified"):
        self.name = student_name
        self.pronouns = pronouns
        self.grades = {}

    def introduce(self):
        print(f"Hi! My name is {self.name}. My pronouns are {self.pronouns}.")

    def add_grade(self, assignment, grade):
        self.grades[assignment] = grade

    def __repr__(self):
        return f"<HackbrightStudent name={self.name} pronouns={self.pronouns}>"
