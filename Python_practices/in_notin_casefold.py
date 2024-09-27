name = "DHANUSH Aravindhan"

letter = input("Enter the string: ").casefold()

# if letter in name.casefold():
#     print("The entered string/character is in name")
#
# else:
#     print("Its not there")

# Casefold method forces to convert the string into lowercase
# It has converted the entire given sting into lower case

if letter not in name.casefold():
     print("Its not there")

else:
    print("The entered string/character is in name")
