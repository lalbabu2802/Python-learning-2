# Conditional Statement :
# in Python perform different computations or actions depending on whether a specific
# Boolean constraint evaluates to true or false. Conditional statements are handled by IF statements in Python.


# What is If Statement? How to Use it?
# In Python, If Statement is used for decision making. It will run the body of code only when IF statement is true.
# When you want to justify one condition while the other condition is not true, then you use "if statement".
# Syntax:
# if expression
#  Statement
# else
#  Statement
from symbol import argument


def main():
    x, y = 8, 8

    if y > x:
        st = "x is less than y"
    elif x == y:
        st = ' x and y are same'

    else:
        st = "x is grater than y"
    print(st)


if __name__ == '__main__':
    main()


# How to execute conditional statement with minimal code
# Syntax:
# 	A If B else C


def fun2():
    a, b = 9, 5
    str1 = "a grater than  b" if a > b else "b is greater than b"
    print(str1)


fun2()

# NESTED IF ELSE

Total = 150
# Country = "Australia"
Country = "United Kingdom"

if Country == "Australia":
    if Total <= 50:
        print("Shipping Cost is 50")
    elif Total <= 100:
        print("Shipping cost is 100")
    elif Total <= 150:
        print("Shipping Cost is 150")
else:
    print("FREE")

if Country == "United Kingdom":
    if Total <= 50:
        print("Shipping Cost in UK is 50")
    elif Total <= 100:
        print("Shipping cost in UK is 100")
    elif Total <= 150:
        print("Shipping Cost in UK is 150")
else:
    print("FREE")


# SWITCH STATEMENT
# A switch statement is a multiway branch statement that compares the value of
# a variable to the values specified in case statements.
# Python language doesn’t have a switch statement.
# Python uses dictionary mapping to implement switch statement in Python


def switchexample(argument):
    switcher = {
        1: "case 01",
        2: "case 02 ",
        3: "case 03"
    }
    return switcher.get(argument, "nothing")


if __name__ == '__main__':
    argument = 2
    print(switchexample(argument))
