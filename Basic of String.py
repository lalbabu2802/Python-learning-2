# Python does not support a character type, these are treated as strings of length one, also considered as substring.
# Various String Operations
# 1. [], [ : }
var1 = "Lalbabu"
var2 = "Chaudhary"

print("var1[0]", var1[0])
print("var2[1:4]", var2[1:4])

# 2.String Concatenation
string1 = var1 + " " + var2
print(string1)

string2 = var1 * 2
print(string2)

# IN / NOT IN operation

x = "lalbabu"
print("a" in x)
print("a" not in x)

# % used for string format
name = "Ajay"
title = 99

print("%s %d" %( name, title))

# some more example

Var = "Hello World!!"
print(Var[6])
print(Var[:6])
print(Var[0:6] + "Lal Babu Chaudhary")

# Python String repalce() methdod
oldstring = "I have my food earlier today"
newstring = oldstring.replace("have", "had")
print( newstring)

# Changing upper and lower case Strings in Python
String12 = "this is my country"
print(String12.upper())

#for capitalizing first letter of String:
String13 = "this is great place for all of us"
print(String13.capitalize())


# string to lower case

String14 = "THIS IS FOR LOWER CASE TEST"
print(String14.lower())

# Join function() 1. print : after every character
print(":" .join("lalbabu"))

# Reverse function
String15 = "1234500"
print("".join(reversed(String15)))


# Split strings
var11 = "lalbabu is lalbabu"
print(var11.split("a"))

# In Python, Strings are immutable.
String16 = "flower"
String16.replace("Flower","cat")  #diff check with clode below
print(String16)

String16 =String16.replace("flower", "CAT") #diff check with clode Above
print(String16)
