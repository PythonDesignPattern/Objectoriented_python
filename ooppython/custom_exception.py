# ---------- CUSTOM EXCEPTIONS ----------

# Lets trigger an exception if the user enters a
# name that contains a number

# Although you won't commonly create your own exceptions
# this is how you do it

# Create a class that inherits from Exception
class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):
        # Raise your own exception
        # You can raise the built in exceptions as well
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")
