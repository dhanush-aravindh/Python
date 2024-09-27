# search in Google --> Mutable sequence types in python3
# and read the python documentation
List1 = [1, 3, 5, 7, 6]
List2 = [2, 4, 8, 10, 9]

print(max(List1))
print(max(List2))
print(min(List1))
print(min(List2))
print()
print(len(List1))
print(len(List2))
print()
print(len("mississippi"))
print(max("mississippi"))
print(min("mississippi"))
print("mississippi".count('s'))
print("mississippi".count('iss'))









































































# Name = input("Enter the Name: ")
# New_name = Name.strip(' ')
# print(New_name)

def length_without_spaces(name):
    return len(name.replace(" ", ""))

# Test the function
name = input("Enter the Name: ")
length_without_spaces_result = length_without_spaces(name)
print("Length of the name without spaces:", length_without_spaces_result)


def length_without_spaces(name):
    count = 0
    for char in name:
        if char != " ":
            count += 1
    return count

# Test the function
name = input("Enter the name:")
length_without_spaces_result = length_without_spaces(name)
print("Length of the name without spaces:", length_without_spaces_result)

