grocery_bag = [
               ["bread","butter"],#1 <- Running in backward loop
               ["bread","butter","Unavailable","cream"],#2 <-Running in backward loop
               ["bread","butter","cream","Unavailable","corn","Unavailable"],# 3
               ["bread","butter","cream","corn","apple","Unavailable","Unavailable"],#4
               ["bread","butter","cream","corn","apple","Tea Bag"],#5

               ]

# Use case:
# We want to order items in the list probably we have added the items in the list
# and one hour later all of those items becomes unavailable.
# Before checkout, the grocer shop or big basket want to show us all the items in the cart.
# There are four items that are unavailable.
# for item in grocery_bag:
#     if "Unavailable" not in item:
#         print(item)
#
#         for inneritem in item:
#             print(inneritem)
#
#     else:
#         print("The list {0} contains, Unavailable: {1} times".format(item,item.count("Unavailable"))) # we can use this code to count the number 4
# The above line is a backend code it can either in java or  python to show the number of items unavailable.It will be much more complex
# The basic idea would be this

# Removing Unavailable items from the list
# If we want to delete something we have to iterate backward.
# I want to delete or ignore the item Unavailable completely.

# for item in grocery_bag: # This for loop runs in forward direction
#     for index in range(len(item)-1,-1,-1): # it runs in backward direction. It will be starting only from first inner list not from last
#         if item[index] == "Unavailable":
#             del item[index]
#     print(item)
# print(grocery_bag)

# Another way is by accessing each and every elements in the inner list:
# for item in grocery_bag:
#     for inneritem in item:
#         if inneritem != "Unavailable":
#             #print(inneritem,end = " ")
#             print(inneritem,end= ",")
#     print()

for item in grocery_bag:
    value = ",".join(value for value in item if value != "Unavailable")
    print([value])
    #print(item)
print()

# How nested List works and Style guides?
empty_list = []
even = [2, 4, 6, 8]
odd =  [1, 3, 5, 7, 9]

numbers= [even , odd] # List with inner lists of odd and even lists which we created it is called nested list
print(numbers)

# How we are going to print nested list using nested for loop:

for numbers_list in numbers:
    print(numbers_list)

    for value in numbers_list:
        print(value)

# PEP-8 guide in python:
# It is a style guide for python. How we will styple our python code

# list=['Python','Java','c','c++',['wipro','infosys',['IBM','cognizant'],'verizon'],'TCS']
# print(list[4][0][1])
#
# print(list[4][2][1])

# list=[3,5,7,9,11,13]
# list.append(15)
# list.extend([3,9])
# list.pop()
# list.insert(3,19)
# print(len(list))
print("+"*35)


list=[3,5,7,9,11]
for i in range(0,len(list)):
    if(i%2==0):
        print(list[i])


print("+"*35)

list = [1,3,5,7]

# del list[1]
#
#list.pop(1)
#list.remove(3)
# list.clear(3)
# print(list)

# list1=['python','java','c']
# list2=[]
# for i in list1:
#     list2.append(i.capitalize())
# print(list2)


list1 = []
list1.append([1, [2, 3], 4])
list1.extend([7, 8, 9])
print(list1)

l=[1,3,5]
m=['a','c','e']
for i in l:
    for j in m:
        if(l.index(i)==m.index(j)):
            print(i*j,end=" ")


# a=['chocolate','biscuit','13','15',['1','5','9'],'coffee']
# for i in a:
#     if(i.isdigit()):
#         if(int(i)%2!=0):
#             print(i,end=" ")


# l = ['sat', 'bat', 'cat', 'mat']
# list(map(list,l))
# print(len(test)**2)

import math
x=[301.16,400.71,500.8,530.71]
s=0
for i in x:
    s+=math.ceil(i)
print(s)

