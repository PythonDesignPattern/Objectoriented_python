# coding=utf-8
class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def get_content(self):
        return self.__content

# By declaring your data member private you mean,
# that nobody should be able to access it from outside the class,
# i.e. strong you can’t touch this policy. Python supports a technique
#  called name mangling. This feature turns every member name prefixed
# with at least two underscores and suffixed with at most one underscore into _<className><memberName> .

redCup = Cup("red")
redCup._Cup__content = "tea"
print redCup.get_content()
