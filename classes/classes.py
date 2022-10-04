class Student:
    """A student at Hackbright."""

    hours_per_week = 40

    def __init__(self, student_name, pronouns='undeclared'):
        """Initialize the attributes of a new Student instance."""

        self.name = student_name
        self.pronouns = pronouns
        self.grades = {}

    def __repr__(self):
        """Return a string representation of the Student instance."""

        return f'<class Student name={self.name}>'

    def add_grade(self, assignment_name, grade):
        """Add an assignment and grade to the student."""

        self.grades[assignment_name] = grade

    def graduate(self):
        """Give the student a doctorate."""

        self.name = f'Dr. {self.name}'

        # the graduate should greet everyone with their new name:
        self.greet()

    def greet(self):
        """Print a custome greeting from the student."""

        print(f'Hi! My name is {self.name}. I\'m here {self.hours_per_week} hours per week.')

    def get_my_id(self):
        """Print the id of the Student instance."""

        print(id(self))

# initialize a new Student instance:
marie_claire = Student('Marie-Claire')

# now that the __init__ method assigns the instance attributes, we no longer
# need to do this:
# marie_claire.name = 'Marie-Claire'

# call the greet instance method:
marie_claire.greet()

# compare the id of the variable with the id of the instance referenced by
# self (they're the same):
print(id(marie_claire))
marie_claire.get_my_id()

# call the graduate method:
marie_claire.graduate()

# compare the grades attribute before and after calling add_grade:
print(marie_claire.grades)
marie_claire.add_grade('assessment1', 100)
print(marie_claire.grades)

# demo the __repr__ method working in the background:
print(marie_claire)
