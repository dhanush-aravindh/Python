# Variables and Types
# A variable name must start with a letter  or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscore (A-z, 0-9, and _)
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Legal Varaible names:
# myvar = "PrepInsta"
# my_var = "PrepInsta"
# _my_var = "PrepInsta"
# myVar = "PrepInsta"
# MYVAR = "PrepInsta"
# myvar2 = "PrepInsta"

# Illegal Variable names:
# 2myvar = "PrepInsta"
# my-var = "PrepInsta"
# my var = "PrepInsta"

# Finding the type of variable
# print(type(variable_name))
string1 = "PrepInsta"
print(type(string1))
print(type("Prepster")) # Object of type 'str' means string
print(type(10)) # Object of type 'int' means integer
print(type(5.6)) # Object of type 'float' which represents decimal values

# Assign variable to multiple values
# Valid Syntax:
# x, y, z = "PrepInsta", "is", "Great"
# print(x)
# print(y)
# print(z)

x1 = "PrepInsta"
y1 = "is"
z1 = "Great"
print(x1 +' ' + y1 + ' ' + z1)

x = "PrepInsta"
y, z ="is","Great"
print(x +' ' + y + ' ' + z)

# Illegal syntax or illegal literals
# Case1:
# x = "PrepInsta", y, z ="is","Great"
# print(x +' ' + y + ' ' + z)
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 40
# x = "PrepInsta", y, z ="is", "Great"
# ^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# Case2:
# x, y, z = "is", "Great"
# print(x +' ' + y + ' ' + z)
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 41, in <module>
#     x, y, z = "is", "Great"
#     ^^^^^^^
# ValueError: not enough values to unpack (expected 3, got 2)

# a=1,b=2,c=3
# print(a+b+c)
# "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\venv\Dhanush\Python\Scripts\python.exe"
# "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py"
#   File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 61
#     a=1,b=2,c=3
# IndentationError: unexpected indent

# a, b, c = "PrepInsta","is",7
# print ( a +' '+ b + ' ' + c)
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 70, in <module>
#     print ( a +' '+ b + ' ' + c)
#             ~~~~~~~~~~~~~~~~^~~
# TypeError: can only concatenate str (not "int") to str

a, b, c = "PrepInsta","is",7
print( a +' '+ b )
print(c)

u = "PrepInsta"
print(u + " is Great")

v = "PrepInsta"
w = " is Great"
Z = v + w
print(Z)

A = 5
B = 6
C = A + B
print(C)

# A1 = 5
# B1 = "PrepInsta"
# C1 = A1+B1
# print(C1)
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 95, in <module>
#     C1 = A1+B1
#          ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Python is a strongly typed language

# A1 = 5
# B1 = "PrepInsta"
# print(A1 + B1)
#  File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 105, in <module>
#     print(A1 + B1)
#           ~~~^~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Python is Strongly typed
# Python is strongly typed as the interpreter keeps track of all variables types
# It's also very dynamic as it rarely uses what it knows to limit variable usage
# In Python, it's the program's responsibility to use built-in-functions like
# isinstance() and issubclass() to test variable types and correct usage.
# Python tries to stay out of your way while giving you all you need to implement strong
# type checking
# Python doesn't give error at compile time but it gives at run time
# isinstance() and issubclass() are the two build in function which is used in the backend while executing a variable

d = isinstance("Dhanush",str)
print(d)
e = issubclass(str,str)
print(e)
p = "Cool"
q = " PrepInsta"
print(p + q)



r = 5
s = 5.5
print(r + s)

a2 = 5
b2 = 10
print(a2 + b2)
# 'float' is subclass of type 'int'
# We can add two numeric datatypes together eg; int,float,decimal,complex
# string datatypes is 'str'
# we cannot merge string and numeric datatypes


# In weekly typed language a compiler / Interpreter will sometimes change the type of a variable
# For example, in some languages (like JavaScript) you can add strings to numbers 'x'+ 3 becomes'x3'.
# This can be a problem because if you have made a mistake in your program, instead of raising an exception execution
# will continue but your variable now have wrong and unexpected values.
# In a strongly typed language (like python) you can't perform operations inappropriate to the
# type of the object-attempting to add numbers to strings will fail.
# Problems like these are easier to diagnose because the exception is raised at the point
# where the error occurs rather that at some other, potentially far removed, place.

# Following are Data Types in Python
# 1. Numeric  2.Iterator  3. Sequence(which are also iterators)  4. Mapping   5. File   6.Class  7.Exception
# We already seen sequence type as str (Strings)
# We would be looking at numeric data types now.

# Python 3 has following data types
# int , float, complex
# Python 2 had long data types to store large values but in python 3, it has been replaced by int
# In Python 3, there is effectively no limit to how long an integer value can be.
# Of course, it is considered by the amount of memory our system has, as are all things
# But beyond that an integer can be as long as you need it to be:
# Numbers without decimal part is considered as 'int' data type
# Numbers with decimal part is called 'float' data type
# Integer limit in C is (-32,768 to 32,767)
# There is no limit for integer value in python (maximum and minimum value is unknown)
# Int:
# Numbers having no decimals
# like 2,10023,-786,0x69,-0x260,0O20,0o29
# Supports
# Decimals(1,-20,100003,-289181) these are numbers without decimal values
# Binary(0b10,0B1120,-0b10)
# Octal (0O10,0o10)
# Hexadecimal(0x69,-0x260)
print(type(10))
print(type(0b10)) # It represents number  2 in decimal
print(type(0b100)) # It represents number 4 in decimal
print(0b10,0b100)
print(0B100)
print(type(0B100))
# Binary prefix is 0b or 0B
# Octal prefix is 0o or 0O
print(type(0o10))
print(0o10) # It represents the number 8
print(0x69)
print(type(0x69))
# hex() this function converts integer numbers,binary,octal into hexadecimal and it writtens the value in string format
# string or 'str'
print(hex(10))
print(hex(15))
print(hex(0o15))

# print(hex(2.5))
#  File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 185, in <module>
#     print(hex(2.5))
#           ^^^^^^^^
# TypeError: 'float' object cannot be interpreted as an integer


print("The number is:" + hex(0o15)) # hex() written type is 'str' so that we can concatenate the hex() with a string
# Every in-build function in python has a written type
print(type(hex(0o15)))

# float
# float values are the ones which have decimals
# Int operations in system memory are faster than float
# The max float value for 64 bit system in python would be:
# 1.7976931348623157e+308, which means shifting decimals 308 places to the right
# Python will indicate a number greater than that by string inf
deci = 1.79e5
print(deci) # 179000.0
# a.be5 e5--> we have to move the decimals 5 points to the right
d1=1.79e308 # Returns the largest number
d2=1.80e308 # Returns infinity
print(d1)
print(d2)
print(d1+d2)

# The closest a nonzero number can be to zero is approximately
# 2.2250738585072014e-308.
# Anything closer to zero than that is effectively zero

# Floating point numbers are represented internally as binary (base-2) fractions.
# Most decimal fractions cannot be represented exactly as binary fractions, so in most cases the internal representation
# of a floating-point number is an approximation of the actual value.
# In Practice, the difference between the actual value and the represented value is very small and should not usually
# cause significant problems
d3 = 2.22e-308
print(d3)
d4 = 0.22e-308
print(d4)
d5 = 0.22e-3010
print(d5)
# The number apart from 2.22e-308  if we further increase the decimal values or zeros beyond this limit it will
# The value will be round off to zero

d6 = 5.999998
print(float(d6))

# If we store a decimal float number in a variable which is having to many decimal values internally it is not stored
# as decimal rather than it is stored as a binary of the number or binary fractions
# When it stores like a binary number so a lot of approximations happen internally we shouldn't be carrying much about
# Since it is stored in binary there is some approximation happening because there is some limited precision
# So there is a small difference between the actual value and representative value
# Python has 52 digits of precision
# If we want more than use  Decimal which is now included in the python,
# but it is not generally used and we won't be talking about it
# In C & C++ float has 6 precision
d7 = 5.123123123123123123123123123
print(d7)  # 5.123123123123123
# Python displays the first 52 digits of the decimal number which can be more than n numbers .Due to the code editor it
# is displaying limited value
d8 = 5.1341345668712346906380749506492539251
print(d8)  # 5.134134566871235
# Numeric Datatypes :
# int,float,complex,decimal(deprecated)

e = 12
f = 3
print(e+f)  # 15
print(e-f)  # 9
print(e*f)  # 36
print(e/f)  # 4.0
print(e//f) # 4
print(e % f) # 0

g = 12
h = 7
print(g+h)
print(g-h)
print(g*h)
print(g/h)
print(g//h)
print(g % h)

for i in range(0,6):
    print(i)

# for i in range(0,e/f):
   # print(i)
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Variables_&_Datatypes.py", line 274, in <module>
#     for i in range(0,e/f):
#              ^^^^^^^^^^^^
# TypeError: 'float' object cannot be interpreted as an integer

for i in range(0,e//f):
    print(i)

# Operator Precedence for C and C++ for practice
positive_infinity= float('inf')
print(positive_infinity)

negative_infinity = float('-inf')
print(negative_infinity)

z = 1.79*10**308 + 1.79*10**308
print(z)
