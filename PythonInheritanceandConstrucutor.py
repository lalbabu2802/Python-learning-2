# Inheritance is a feature used in object-oriented programming;
# it refers to defining a new class with less or no modification to an existing class.
# The new class is called derived class and from one which it inherits is called the base.
# Python supports inheritance; it also supports multiple inheritances.
# A class can inherit attributes and behavior methods from another class called subclass or heir class.


class MyBaseClass:

    def methodbase1(self):
        print("This is method 1 of Base class: ")

    def methodbase2(self):
        print("This is method 2 of Base class: ")


class ChildClass(MyBaseClass):
    #

    def childmethod1(self):
        MyBaseClass.methodbase1(self)
       # print("this is in child class1 : Method base class1 ")

    def childmethod2(self):
        print("this is in child class method 2")


def main():
    k = ChildClass()
    k.childmethod1()
    k.methodbase2()
    k.childmethod2()


main()


# Python Constructors
# A constructor is a class function that instantiates an object to predefined values.
# It begins with a double underscore (_). It __init__() method

class Test:
    name = ""

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Say HEllO to : " + self.name)


user1 = Test("lalbabu")
user1.hello()






