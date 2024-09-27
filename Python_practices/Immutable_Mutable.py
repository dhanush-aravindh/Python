# Immutable vs Mutable objects in Python
# Immutable Objects
# When a object is Immutable means, it can't  be changed
# 1. Int
# 2. Float
# 3. Bool(subset of int)
# 4. Str(String)
# 5. Tuple
# 6. Frozen set & Byts
# Example:
# An int value like : 15 can't be changed, 15 is 15 and we can add 1 to 15 to get 16
# But we can't change 15.
# Similarly, Pi is 3.1415, we can add something to this, but we can't change it.
# Bool values also
# And Strings as well
# Python says, that ID, shouldn't necessarily be objects address.
# It only says that, ID must not change, throughout the lifetime and it must be guaranteed.
# --> Cpython however,returns the address but not all versions of python will do that
# --> However,if Python has to destroy the object and create it again, then obv. It will change
# --> The ID of an object, can change everytime you run the program again,
# however, while the program is running it won't change.

print(id(list))
print(id(list))
print(id(str))
print(id(tuple))
print(id(dict))
print(id(set))
print(id(frozenset))
print(id(bytes))
# In Python, whenever we create an object it gets associated with the ID
# In C & C++, the object created gets associated to address
# In Python, whenever the object is attached to the ID. It doesn't need to be the object address.
# It says that ID isn't unique reference to the object, and it will remain the same.
print(dir(frozenset))
print(dir(bytes))

# In C or C++ the object is assigned by the address
# result object is assigned with an address of 4000
# another_result will be assigned an object of 4001
result = True
#another_result = result
print(id(result))
#print(id(another_result))
print()
# How come the both the objects are having the same ID.
# It has created memory for the value True and what it is doing is it is binding the name result with the value True.
# Later we can change the value of another_result at that it will be assigned a new ID value.
# The variable names are references for the particular value.
result = False
print(id(result))
print()
# Basically this is immutable. We can't change the value
# But if we are trying to change the value in that case we will create a new ID
# 4000 =10 -->  C or C++
# 10 = 140705896588360 ----binded---(result) -->Python
# The above address will be debinded and re-binded by the new address
result = 10
print(id(result))
print()
# 4000 =11 ---> C or C++
# 11  = 140705896588392---re-binding---(result) -->Python
result = 11
print(id(result))
print()
# ID and address are same thing in Cpython
# In C or C++ have the same address of the object if we change the value of the object
# In python, we are binding the address value with the variable
# If we are changing the value of the variable in python first we debind the ID from the previous value and
# the variable is then re-binded with new address value.

result = "PrepInsta"
print(result)
print(id(result))

print()

result += " Prime"
print(result)
print(id(result))

# PrepInsta ---> This value has one address
# 1823914414832
# We have two values
# PrepInsta Prime --> This value has created a new address
# 1823914414512
# Both PrepInsta and PrepInsta Prime are different values with different addresses
# If we try to change the value contained in an immutable object, so rather than the object updating
# its own value, a new ID/address(cpython) is created for  that new value and the immutable object is unbinded
# from previous ID and binded now, the  new ID of value.

#x = """PrepInsta's special course"""
x = ""'PrepInsta\'s special course'""
print(x)

# Mutable objects
# Mutable is any object , whose value can be changed
# 1. List
# 2. Dict
# 3. Set
# 4. Bytearray
# We can change the value of mutable objects,without even,
# having the need to destory or re-create it.

# grocery = ["eggs","coffee","milk","bread"]
# another_grocery = grocery
# print(grocery)
# print(id(grocery))
# print(another_grocery)
# print(id(another_grocery))
# print()
# grocery += ["tea"]
# print(grocery)
# print(id(grocery))
# print(another_grocery)
# print(id(another_grocery))
# We have added tea to grocery but it added automatically to another grocery.
# Whenever we are working with immutable objects it is not the problem
# Whenever we are working with mutable objects it is an issue.

# solving mutability issue with copy() method
# Here we are facing the problem the address or ID created for the same set of values
# However, we can reference the ID or address with two names
# The two where grocery and another_grocery.
# we are refering the same ID with two different names.
# In other make the ID and names to be different we can the copy method
print()
grocery = ["eggs","coffee","milk","bread"]
another_grocery = grocery.copy()
print(grocery)
print(id(grocery))
print(another_grocery)
print(id(another_grocery))
print()
grocery += ["tea"]
print(grocery)
print(id(grocery))
print(another_grocery)
print(id(another_grocery))

print()
print(grocery,id(grocery))
print("The items are : {} and the ID is {}".format(grocery,id(grocery)))
print("The items are : {0} and {0} the ID is {1}".format(grocery,id(grocery)))
# Coding is like mathematics
