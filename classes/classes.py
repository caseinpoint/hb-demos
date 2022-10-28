class BaseHackbrighter:
    """A person at Hackbright."""

    greeting = 'Hey!'
    role = None

    def __init__(self, name, pronouns='undeclared'):
        """Initialize the attributes of a new Hackbrighter instance."""

        self.name = name
        self.pronouns = pronouns

    def greet(self):
        """Print a custom greeting from the Hackbrighter."""

        print(f'{self.greeting} My name is {self.name}. My pronouns are {self.pronouns}.')


class Student(BaseHackbrighter):
    """A student at Hackbright."""

    greeting = 'Hi there!'
    role = 'Student'

    def __init__(self, name, pronouns='she/her'):
        """Initialize the attributes of a new Student instance."""

        super().__init__(name, pronouns)

        # Grades are unique to the Student class, so that's why we should
        # override the __init__ method. Grades are also unique to each
        # individual student, so that's why it should be an instance attribute
        # instead of a class attribute.
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

    def get_my_id(self):
        """Print the id of the Student instance."""

        print(id(self))


class Instructor(BaseHackbrighter):
    """An instructor at Hackbright."""

    greeting = 'Greetings and salutations!'
    role = 'Instructor'

    def __init__(self, name, pronouns='undeclared'):
        """Initialize the attributes of a new Instructor instance."""

        super().__init__(name, 'Instructor', pronouns)

        # self.students should be a list of Student objects (composition
        # rather than inheritance)
        self.students = []


# initialize a new Student instance:
marie_claire = Student('Marie-Claire', 'she/her')

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
