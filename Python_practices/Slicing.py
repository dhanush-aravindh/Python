#                    11111
#          012345678901234
String1 = "Prepinsta Prime"
#        -15            -1
#     0 1 2 3 is printed and 4 is not included
print(String1[0:4])
# It starts to print from Zero index position and goes upto third position excluding the 4th index position
print(String1[5:11])
print(String1[0:9])
print(String1[:9])
print()
print(String1[10:15])
print(String1[10:])
print()
print(String1[:9])
print(String1[10:])
print()
print(String1[:9]+String1[9:])
print()

# Negative Slicing:
print(String1[10-15])
print(String1[-5:2])
# We cannot print in backward direction we can only print in forward direction
print(String1[-5:-2])
print(String1[-5:-15]) # No backward direction is allowed
print(String1[-15:-5]) # Only forward direction is allowed
# During Slicing [a:b] the value gets printed from value a and goes up to the value before b and value of b is not included
# a--> Start value and b--> end value
print(String1[-5:13])
print(String1[-5:])
