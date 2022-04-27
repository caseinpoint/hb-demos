class Number:
    """A number."""

    def __init__(self, value=1):
        self.value = value

    def result(self):
        return self.value

    def add(self, num=1):
        self.value += num

class SameNumber(Number):
    """Returns the same instance for chaining."""

    def add(self, num=1):
        self.value += num
        return self

class NewNumber(Number):
    """Returns a new instance for chaining.
    
    (This is similar to how flask_sqlalchemy.BaseQuery works)"""

    def add(self, num=1):
        new_num = self.value + num
        return NewNumber(value=new_num)