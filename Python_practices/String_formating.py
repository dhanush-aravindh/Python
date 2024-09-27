# In range() function the end value is not included: it will print from start value to endvalue-1
for i in range(1,11):
    print("No. {0} squared is {1} and cubed is {2}".format(i,i**2,i**3))
    print("No. {0} squared is {1} and cubed is {2}".format(i,pow(i,2),pow(i,3)))
print()

# In order to improve the readability of the code:
for i in range(1,11):
    print("No.{0:2} squared is {1:3} and cubed is {2:4}".format(i,i**2,i**3))

# Whatever the number may be represented using {0:2} atlest we should have 2 character spaces that is significance
# of :2 in string replacement field.
# We are telling to our program is  that whatever the output use atlest two character space to print it {0:2}
print()
for i in range(1,11):
    print("No.{0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))

# using < less than symbol we tell out  editor to left align the items
# Middle align we need to use power or up-top arrow operator ^
# Using < symbol we tell our editor to left align items
# Using ^ symbol we tell our editor to middle align items
# By default we have right align