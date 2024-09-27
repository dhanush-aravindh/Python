# The default precision in python after decimals is 15
# Ctrl + D is the shortcut to copy the same line of code to the next line
print("{0}".format(22/7))
print(len("{0}".format(22/7)))
print()
print("{0:100}".format(22/7))
print(len("{0:100}".format(22/7)))
print()
# we are telling the compiler must print 100 characters where ever the string is going to be printed
# By default it gives values on the right hand side
print("{0:<100}".format(22/7))
print(len("{0:<100}".format(22/7)))
# we can also left align the values
# fill with atleast 100 characters
print("{0:0100}".format(22/7))
print("{0:1100}".format(22/7))
print("{0:-100}".format(22/7)) # No change
print()
# It will allows the compiler to create 1100 character spaces to be empty
# print("{0:a100}".format(22/7))
#  File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Precision.py", line 16, in <module>
#     print("{0:a100}".format(22/7))
#           ^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: Invalid format specifier 'a100' for object of type 'float'
# It fills all the empty spaces with zero only zero is allowed apart from other characters are not allowed
# The above examples illustrates the basic practices of fill with

print("{0:100f}".format(22/7))
print("{0:100.2f}".format(22/7))
# It contains a maximum of 100 bit values and only 6 digits are printed after the precision/Decimal point
# rather than by default version of python which is 15
# Python is greatly inspired from C and C++
# The default precision float values in C is 6 digits and then it was doubled in case of python 15
# f=6--> If we use just use f then we mean after decimal points there must be 6 character after decimal
print("{0:100f}".format(2/1)) # -->2.0
print("{0:100f}".format(2//1)) # -->2
# .2f --> prints 2 values after decimal point. Essentially we are forcing the compiler to print 2 values eventhough we
# have 6 values we are telling the editor to avoid other values apart from 2 values after the decimal
print("{0:.2f}".format(22/7))
print("{0:.8f}".format(22/7))
print("{0:.8}".format(22/7))
print("{0:2f}".format(22/7))
print("{0:.2}".format(22/7))
print()
print("{0:0100f}".format(22/7))
print("{0:0100.2f}".format(22/7))
print()
# Precision takes more importance/precedence than filled with
print("{0:3.6f}".format(22/7))
# The maximum decimal precision value in python is 51 or 52 or 53 or 54 --> 51 characters after decimal
print("{0:.70f}".format(22/7))
print("{0:100.70f}".format(22/7))
print("{0:3.70f}".format(22/7))
# If we provide more precision than the maximum precision value in python automatically it starts to get additional
# value with zero after reaching the maximum precision value





