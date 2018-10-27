# A Functions in Python are used to utilize the code in more than one place in a program,
#  sometimes also called method or procedures.
#  Python provides you many inbuilt functions like print(),
#  but it also gives freedom to create your own functions.


# How to define and call a function in Python
# Function in Python is defined by the "def " statement followed by the function name and parentheses ( () )


def func1():  # function definition
    print("this is inside a function\n")
    print("this is 2nd statement in function\n")


func1()  # function call


# Significance of Indentation (Space) in Python
# Python follows a particular style of indentation to define the code
# since Python functions don't have any explicit begin or end like curly braces to indicate,
# the start and stop for the function, they have to rely on this indentation
# At least, one indent is enough to make your code work successfully.
# But as a best practice it is advisable to leave about 3-4 indent to call your function.

def func2():  # function definition
    print("this is inside 2 function\n")
    print("this is 2nd statement in 2 function\n")


func2()


# How Function Return Value?

# Return command in Python specifies what value to give back to the caller of the function.

def square(x):
    return x * x  # gives output not nun
    # print(x * x)


print(square(4))
print(square)


# Functions in Python are themselves an object, and an object has some value.
# We will here see how Python treats an object. When you run the command "print square"
#  it returns the value of the object. Since we have not passed any argument,
#  we don't have any specific function to run over here it returns a default value (an address)
#  which is the location of the object

# Arguments in Functions:
# The argument is a value that is passed to the function when it's called.
# In other words on the calling side, it is an argument and on the function side it is a parameter.

# Step 1) Arguments are declared in the function definition.
# While calling the function, you can pass the values for that args as shown below

def multiply(x, y):  # Declaring Arguments
    # print(x * y)

    return x * y


print(multiply(4, 5))  # Passing Arguments
print(multiply(y=6, x=3))  # change the arguments order like this


# multiply(2, 4)  # Passing Arguments

# Multiple Arguments can also be passed as an array.
# Here in the example we call the multiple args (1,2,3,4,5) by calling the (*args) function

def lbc(*args):
    print(args)


lbc(1, 2, 3, 4, 5)
