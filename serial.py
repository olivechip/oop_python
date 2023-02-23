"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()
    'Number was reset back to 100!'

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Starts the generator at the input number"""
        self.start = start
        self.next = self.start
    
    def __repr__(self):
        return f"SerialGenerator: start={self.start} next={self.next}"

    def generate(self):
        """Returns the current number and prepares the next number"""
        self.next += 1
        return self.next -1

    def reset(self):
        """Resets the number back to the input number"""
        self.next = self.start
        return f"Number was reset back to {self.start}!"