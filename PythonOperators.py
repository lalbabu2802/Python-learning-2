# This section is about Operators in Python

# Arithmetic Operators
# Comparison Operators
# Python Assignment Operators
# Logical Operators or Bitwise Operators
# Membership Operators
# Identity Operators
# Operator precedence

# 1.Arithmetic Operators perform various arithmetic calculations like addition, subtraction, multiplication, division,
# %modulus, exponent, etc.

x = 20
y = 5
print("addition: %d" % (x+y))
print(x-y)
print(y-x)
print(x*y)
print(x/y)
print(x % y)
print(y % x)


# 2. Comparison Operators: These operators compare the values on either side of the operand and determine the
# relation between them. It is also referred as relational operators. Various comparison operators are ( ==, != , <>,
#  >,<=, etc)
print("x is grater than y: %s" % (x > y))
print("y is greater than x: %s" % (y > x))
print("x is equal to  y: %s" % (x == y))
print("x is not equal to  y: %s" % (x != y))
print("x is grater than y: %d" % (y <= x))  # to print 1 or 0 use %d

# 3.Assignment Operators: are used for assigning the value of the right operand to the left operand.
#  Various assignment operators used in Python are (+=, - = , *=, /= , etc.)

Number1 = 21
Number2 = 42

print("Value Assigned in Line 1 to Variable Number1 is : %s" % Number1)
result1 = Number1 + Number2

# 3.1 Compound Assginment Operature:
Number1 = 21
Number2 = 42
result1 = Number1 + Number2
result2 = Number1 * Number2

print("Value Assigned in Variable result1 is : %s" % result1)
print("Value Assigned in Variable result2 is : %s" % result2)

# 4. Logical Operators:  are used for conditional statements are true or false.
#  Logical operators in Python are AND, OR and NOT. For logical operators following condition are applied.
# ->For AND operator – It returns TRUE if both the operands (right side and left side) are true
# ->For OR operator- It returns TRUE if either of the operand (right side or left side) is true
# ->For NOT operator- returns TRUE if operand is false
a = True
b = False
c = True

print("a and b: %s" % (a and b))
print("a or b: %s" % (a or b))
print("NOT a: %s" % (not a))
print("a and c: %s" % (a and c))
print("a or c: %s" % (a or c))
print("NOT b: %s" % (not b))

# 5.Membership Operators: These operators test for membership in a sequence such as lists, strings or tuples.
#  There are two membership operators that are used in Python. (in, not in).
#  It gives the result based on the variable present in specified sequence or string

x2 = 5
y2 = 77

List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 5, 4]

if x2 in List1:
    print("x2 : '%d' is present in list" % x2)
else:
    print("x2 is not present in list")

if y2 not in List1:
    print("y2 : '%d' is not present in the given list " % y2)
else:
    print("y2 is not present in the given List")

# 6. Identity Operators:
# To compare the memory location of two objects, Identity Operators are used.
# The two identify operators used in Python are (is, is not).#
# Operator is: It returns true if two variables point the same object and false otherwise
# Operator is not: It returns false if two variables point the same object and true otherwise

variable1 = 100
variable2 = 100
variable3 = 50

if variable1 is variable2:
    print("variable1 and variable2 have same identity")
else:
    print("variable1 and variable2 have different identity")

if variable1 is not variable3:
    print("variable1 and variable3 have different identity")
else:
    print("variable1 and variable3 have same identity")

# Operator precedence:
# The operator precedence determines which operators need to be evaluated first. To avoid ambiguity in values,
# precedence operators are necessary. Just like in normal multiplication method, multiplication has a higher precedence
# than addition. For example in 3+ 4*5, the answer is 23, to change the order of precedence
# we use a parentheses (3+4)*5, now the answer is 35.
# Precedence operator used in Python are (unary + - ~, **, * / %, + - , &) etc.

var1 = 8
var2 = 2
var3 = 4
var4 = 5
var5 = 0

var5 = (var1 + var2) * var3/var4
print("value of(var1 + var2) * var3/var4 is : %d " % var5)




