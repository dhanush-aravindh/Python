 # The Python 3 has basically  5 sequence types built in
 # The string type
# list
# tuple
# range
# bytes and bytearray

# Sequence
# A sequence is nothing but an orddered set of items
# A string "PrepInsta" contains 9 items and each of them is individual character
# A list is also a sequence type Example of list would be
# eg: ["Orange","Mango","Apple","Guava","PineApple"]
# Everything that we can do with string (str) you can also do with other sequence data types as well
# For now, We will focus on string(str) data types and we will learn more about others later in the course.

String1 = "PrepInsta"
print(String1)
print(String1[0])

for i in String1:
    print(i)  # 'i' is the index

string2 = ["Orange","Apple","Banana"]
print(string2[0])
print(string2[1])

for i in string2:
    print(i)


print(string2[1][3])

String3 = "I am"
String4 = " Studying from"
String5 = " PrepInsta Python"
String6 = " Prime Video course"
print(String3 + String4 + String5 + String6)

print("I am" " Studying from" " PrepInsta Python" " Prime Video course" )
print("I am"+" Studying from"+" PrepInsta Python" + " Prime Video course" )

String7 = "I am" + " Studying from" + " PrepInsta Python" + " Prime Video course"
print(String7)
print()

print("PrepInsta " * 3)
#print("PrepInsta " * 3 + 5)
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\String_operators.py", line 47, in <module>
 #     print("PrepInsta " * 3 + 5)
 #           ~~~~~~~~~~~~~~~~~^~~
 # TypeError: can only concatenate str (not "int") to str

print("PrepInsta " * (3 + 5))
print("PrepInsta " * 3 + "5")
print()

day = "Sunday"
print("day" in day) # True
print("fri" in day) # False
print("Sun" in day) # True
print("sun" in day) # False

print("Aug" in "Augest") # True

