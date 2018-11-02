# A Class is a logical grouping of data and functions.
# It gives the freedom to create data structures that contains arbitrary content
# and hence easily accessible.

# How to define Python classes:
# Step 1) In Python, classes are defined by the "Class" keyword
# Step 2) Inside classes, you can define functions or methods that are part of this class
# Step 3) Everything in a class is indented, just like the code in the function, loop, if statement, etc.
#          Anything not indented is not in the class.
# Step 4) Make an object of the class
# Step 5) Call a method in a class


class MyFirstClass:
    def func1(self):
        print("this is first  methid in class")

    def func2(self, something):
        print("this is second method in this class : " + something)


def main():

    c = MyFirstClass()
    c.func1()
    c.func2("'test for passing parameter something'")


main()
