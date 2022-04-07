class HackbrightStudent:
    """A student at Hackbright."""

    school = "Hackbright Academy"

    def __init__(self, student_name="Balloonicorn", pronouns="unspecified"):
        self.has_graduated = False
        self.name = student_name
        self.pronouns = pronouns

    def __repr__(self):
        return f"<HackbrightStudent name={self.name} pronouns={self.pronouns}>"

    def introduce(self):
        print(f"Hi! My name is {self.name}. My pronouns are {self.pronouns}.")

        if not self.has_graduated:
            print(f"I am a student at {self.school}")
        else:
            print(f"I have graduated from {self.school}")

    def graduate(self):
        self.has_graduated = True
        self.introduce()
