# coding=utf-8
# ---------- STATIC VARIABLES ----------
# Fields declared in a class, but outside of any method
# are static variables. There value is shared by every
# object of that class

class Dog:

    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        # You reference the static variable by proceeding
        # it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():

    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()

    doug.getNumOfDogs()


main()


#
# # ---------- MODULES ----------
# # Your Python programs will contain a main program that
# # includes your main function. Then you will create many
# # modules in separate files. Modules also end with .py
# # just like any other Python file
#
# # ————— sum.py —————
# def getSum(*args):
#     sum = 0
#
#     for i in args:
#         sum += i
#
#     return sum
#
# # ————— End of sum.py —————
#
# # You can import by listing the file name minus the py
# import sum
#
# # Get access to functions by proceeding with the file
# # name and then the function you want
# print("Sum :", sum.getSum(1,2,3,4,5))
#
# # ---------- FROM ----------
#
# # You can use from to copy specific functions from a module
# # You can use from sum import * to import all functions
# # You can import multiple functions by listing them after
# # import separated by commas
# from sum import getSum
#
# # You don't have to reference the module name now
# print("Sum :", getSum(1,2,3,4,5))