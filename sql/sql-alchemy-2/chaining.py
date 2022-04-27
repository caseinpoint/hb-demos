"""A demonstration of two ways to write methods that allow chaining."""

class Number:
    """A number."""

    def __init__(self, value=1):
        self.value = value

    def result(self):
        return self.value

    def add(self, num=1):
        """Increment value by num.
        
        If we were to try to chain these methods, we would get an error:
        >>> n = Number(1)
        >>> n.add(1).result()
        AttributeError: 'NoneType' object has no attribute 'result'
        """

        self.value += num


class SameNumber(Number):
    """A chainable number."""

    def add(self, num=1):
        """Increment value by num.
        
        By returning self, we can chain method calls:
        >>> sn = SameNumber(1)
        >>> sn.add(1).result()
        2
        """

        self.value += num

        return self


class NewNumber(Number):
    """A chainable number."""

    def add(self, num=1):
        """Increment value by num.

        By returning a new instance, we can chain method calls without mutating
        the original instance:
        >>> nn = NewNumber(1)
        >>> nn.add(1).result()
        2
        >>> nn.result()
        1

        (This is similar to how flask_sqlalchemy.BaseQuery works)
        """

        new_num = self.value + num

        return NewNumber(value=new_num)
