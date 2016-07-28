# ---------- PROBLEM EXCEPTIONS & FILES ----------
# 1. Create a file named mydata2.txt and put data in it
# 2. Using what you learned in part 8 and Google to find
# out how to open a file without with try to open the
# file in a try block
# 3. Catch the FileNotFoundError exception
# 4. In else print the file contents
# 5. In finally close the file
# 6. Try to open the nonexistent file mydata3.txt and
# test to see if you caught the exception
from twisted.protocols.ftp import FileNotFoundError

try:
    myFile = open("mydata2.txt", encoding="utf-8")

# We can use as to access data and methods in the
# exception class
except FileNotFoundError as ex:
    print("That file was not found")

    # Print out further data on the exception
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")