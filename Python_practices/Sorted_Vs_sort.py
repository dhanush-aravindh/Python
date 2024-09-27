# Sorted Vs sort
string1 = "Two driven jocks help fax my big quiz" #Pangram
# Pangram --> It is a string which contains all the alphabetical letters in the string

result = sorted(string1)
print(result)

num = [8.9,7.1,1.2,4.1,11.7,2.3]
sorted_num = sorted(num)
print(sorted_num)
print()

# Sort
num = [8.9,7.1,1.2,4.1,11.7,2.3]
sorted_num = num.sort()
print(num)
print(sorted_num)


# Sort:
# It is a method which doesn't return anything to assigned values
# Also sorts the existing string itself

# Sorted:
# It is a function which returns the sorted string and assigned values
# However, the original strings doesn't get sorted (not changed) it remains same
# The sorted string can be accessed using different variable.

# Both sort and sorted functions sorted the values baseed on the ascii value of the elements

List1 =["Mike",
        "Chris",
        "eric",
        "Andy",
        "chole",
        "Joe",
        "Po",
        "Z"
        ]

List1.sort()
List1.sort(key=str.casefold)
print(List1)
# We can also use the key parameter to solve the sorting problems based on ascii value

# Sorted
List2 = sorted(List1,key=str.casefold)
print(List2)

newString = sorted(string1)
print(newString)

newString.sort(key=str.casefold,reverse = True)
print(newString)
# Key is used to represent the sorting should happen according to this rule
# reverse is used to reverse the sorting order
List1.sort(key=str.casefold,reverse=True)
print(List1)

List2= sorted(List1,key=str.casefold,reverse = True)
print(List2)

# We can also sort using our own rule:

def myfunc(e):
    return len(e)

List1.sort(key=myfunc)
print(List1)

List1.sort(key=myfunc,reverse=True)
print(List1)