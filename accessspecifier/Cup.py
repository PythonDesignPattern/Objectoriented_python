class Cup:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def get_color(self):
        return self.color

    def get_content(self):
        return self.content


# Example of Public access specifier in python
# All member variables and methods are public by default in Python.
redCup = Cup()
redCup.color = "red"
print redCup.get_color()
redCup.content = "tea"
print redCup.get_content()
redCup.empty()
print redCup.get_content()
redCup.fill("coffee")
print redCup.get_content()