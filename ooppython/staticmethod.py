# ---------- STATIC METHODS ----------

# Static methods allow access without the need to initialize
# a class. They should be used as utility methods, or when
# a method is needed, but it doesn't make sense for the real
# world object to be able to perform a task

class Sum:

    # You use the static method decorator to define that a
    # method is static
    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():

    # Call a static method by proceeding it with its class
    # name
    print "Sum :", Sum.getSum(1,2,3,4,5)


main()