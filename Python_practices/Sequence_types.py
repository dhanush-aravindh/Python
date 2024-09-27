# Introduction to Sequence Types:
# 1. Lists
# 2. Tuples
# 3. Range
# 4. String

# What is sequence types in Python?
# Sequence is an ordered collection of items
# Now, here having a proper order is very important
# If sequence wasn't ordered, then you couldn't refer them with their index position
# Eg: String1 = "PrepInsta Prime"
# String1[10] or "PrepInsta Prime[10]" will return P always
# Which means, if you iterate over a string any number of times using for / while loop will get the same output always

# Iterable
# Anything that you can iterate over is an iterable
# Basically if you can use a for loop or a while loop with it you can iterate on it
# The correct definition would be-
# If the object contains the following methods then it is an iterable
# __iter__
# __getitem__
# Indexing must also start with 0.
x = [1,23,445]
print(dir(x))
print(dir(list))
print('*'* 115)
print(dir(tuple))
print()
print(dir(str))
print()
print(dir(dict))
print()
print(dir(set))
print()
print(dir(range))
# C Vs Python
# Implementing Data structures required its functions to be explicitly implemented
# Gives ease of implementing data structures with built-in insert,append functions
# It is compulsory to declare the variable tyope in C
# No need to declare a type of variable in python
# C program syntax is harder than python
# Python programs are easier to learn,write and read

# All Sequence types are iterable types
# 1. This is, can be iterated over
# 2. So,string,list,tuple,range are iterable
# However, all iterables are not sequence types
# 1. Example: Dictionary in python can be used in for loop
# 2. But, Dictionary is not a sequence
# We can consider: Iterables are superset of sequence types,
# Sequence type is subset of iterables
# all sequence types are iterable types but all iterable types are not sequence types
# C