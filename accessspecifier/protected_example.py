# coding=utf-8
class cup:
    def __init__(self):
        self.color = None
        self._content = None  # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def get_color(self):
        return self.color

    def get_content(self):
        return self._content

# Protected member is accessible only from within the class and it’s subclasses.


class second_cup():
    def content(self, content):
        cup()._content = content
        print cup().get_content()

cup = cup()
cup._content = "tea"
# print cup.get_content()
print second_cup().content("yes")


