#                    11111
#          012345678901234
String1 = "Prepinsta Prime"
#        -15            -1
print(String1[0:15])
print(String1[-15:0]) # O is not inclueded in negative slicing
print(String1[0:-1])
print(String1[-15:])
print()
print(String1[0:15:2]) # We are incrementing the index values by 2 and printing the corresponding values.

number = "1,789,637,918,718,189,183"
print(number[1::4])

number2 = "1,789:637;918 718:189;183"
sep = number2[1::4]
print(sep)
print()

# Advanced python coding:
# How to control the separators and converting the values into required format
values = "".join(char if char not in sep else " " for char in number2).split()
print([int(val) for val in values])




