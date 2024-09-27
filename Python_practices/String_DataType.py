# String Datatype is a sequence of characters enclosed within '' or ""
#                    11111
#          012345678901234
String1 = "Prepinsta Prime"
#         -15            -1
# In Python Indexing starts from 0 to n-1 or 0 to length of the string - 1
# Positive index starts from Zero
# Negative intex starts from -1. Negative indexing length of the string is (last index value of Positive indexing + 1)

print(String1[10])
print(String1[-1])
print()

# Pit Pie
print(String1[0])
print(String1[4])
print(String1[7])
print()
print(String1[10])
print(String1[12])
print(String1[14])

print()

print(String1[0-15])
print(String1[4-15])
print(String1[7-15])
print()
print(String1[10-15])
print(String1[12-15])
print(String1[14-15])
print()

print(String1[-15])
print(String1[-11])
print(String1[-8])
print()
print(String1[-5])
print(String1[-3])
print(String1[-1])
print()

print(String1)

for i in String1:
    print(i)      # String1[0].......String[14]

print()

print(String1[-15])
print(String1[-11])
print()

print(String1[-15])
print(String1[4-15])
print()

string2 = "P"
print(string2)
print(string2[0])
print(string2[-1])
print()

string3 = "Pr"
print(string3)
print(string3[0])
print(string3[-1])
print(string3[-2])
print()

#string4 = ""
# print(string4[0])
# print(string4[-1])
#  File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\String_DataType.py", line 72, in <module>
#     print(string4[0])
#           ~~~~~~~^^^
# IndexError: string index out of range

String = ""
print(String)

print(0xE + 0xF + 0xD)
print("Hello {name1}{name2}".format(name1='dear', name2='prepster'))
print("The sum of {0:b} and {1:x} is {2:o}".format(12, 1, 10))
print(bin(12))
print(hex(1))
print(0o10+2)
print("Hello {0!r} and {0!s}".format('Prep', 'insta'))
# print('{:,}'.format('2221114443'))
print('{:#}'.format(2221114443))
#print('{:$}'.format(4445552221))
print("Hello {0[0]} and {0[1]}".format(('prep', 'insta')))