# If we want to perform the same task multiple times, for loops comes into picture
for i in range(1,101):
    print("No.{0:3} squared is equal to {1:5} ".format(i,i**2))
    print("*"*33)
# This is called iteration
# Iteration means if we have to run the code for certain 'n' number of times.
# The number of times the code is runned is equal to number of times it is iterated.
# Different ways of Iteration:
# For
# while
# List comprehensions and genrator expressions
# What is a for loop?
# The for loops runs on set of values, which come from a sequence or some iterable objects
# One thing that we have already seen is a string type
# Iterable object is anything that we can run iterations upon.
# Range is also an example of iterable
# Sequence it of string type

# Print each character of the given string
name = input("Enter the string: ")
print(name)
for val in name:
    print(val)


# List comprehension
z = [(i,i**2) for i in range(1,101)]
z1= [{i:i**2} for i in range(1,101)]
print(z)
print(z1)

numbers  = "1,72825663,9103453:163353;128533'123,123"
value = ""
sep = ""
for char in numbers:
    if char.isnumeric():
        value = value + char
print(value)
for char in numbers:
    if not char.isnumeric():
        sep = sep +" "+char
print(sep)
print(int(x) for x in value)
# separator = numbers[1::4]
# print(separator)
#
# values = "".join(char if char not in separator else " " for char in numbers).split()
# print([int(val) for val in values])
# Everytime when we encounter the separator we replace them with else condition in the values
# Debugging for loops:
# we can use toggle point to debug the code and find its execution line by line

# user input:
number =input("Enter the user input:")
values = ""

for i in number:
    if i.isnumeric():
        values = values + i
print(values)
print(sum([int(x) for x in values]))