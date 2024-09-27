# Bad way of writing list:
#grocery = ["eggs","milk","bread","butter","iPhone"]

# Good way of writing list:
#  The below mentioned list is the coding standard for writing the list
# grocery = ["eggs",
#            "milk",
#            "bread",
#            "butter",
#            "iPhone"
#            ]
#
# for item in grocery:
#     print(item)
#
# print()
#
# print(grocery[2])
# print()
# print(grocery[:3])
# print()
# print(grocery[0:5:2])
# print(grocery[-1])
#
# # List most widely used in data science
# # Binding different names with the list
# another_grocery = grocery
#
#
#
# List1 = List2 = List3 = List4 = grocery
#
# grocery.append('tea')
# print()
# grocery.append('sugar')
# print()
# grocery += ['Kettle']
#
# # grocery = grocery + ['Water']
# print(List1,List2,List3,List4)


# One ID in python is assigned with different names
# we know operator precedence starts from right to left

# Appendig to a List
# Want to create an user interface for Choice
# 1. Curd
# 2. Bread
# 12345 all the items are added to the cart
# 0 is entered automatically come out of the cart
# applications like BigBasket and all the items are displayed
# creating an item called choice
choice = "_"
grocery_items = []

# while choice != "0":
#     if choice in "1234":
#         print("Adding {0} to BigBasket Cart".format(choice))
#
#         if choice == "1":
#             grocery_items.append("Butter")
#         if choice == "2":
#             grocery_items.append("Milk")
#         if choice == "3":
#             grocery_items.append("fruits")
#         if choice == "4":
#             grocery_items.append("coffee")
#
#     else:
#         print("Add items from the following available ones: ")
#         print("1. Butter")
#         print("2. Bread")
#         print("3. Milk")
#         print("4. Tea Bag")
#         print("0. Exit")
#
#     choice = input()

#print(grocery_items)


# while choice != "0":
#     choice = input("Enter name of item, you want to add to Big Basket Cart: ")
#
#     if choice != "0":
#         grocery_items.append(choice)
#
# print(grocery_items)

# Iterating over the list
# If the grocery store has more than 1000 items
# Then how will you access that
instock_items = ["Milk",
                 "Curd",
                 "Rice",
                 "Bread",
                 "Coffee",
                 "Butter",
                 "Tea Bag"
                 ]
grocery_items = []
while choice != "0":
    if choice in "1234":
        print("Adding {0} to BigBasket Cart".format(choice))

        if choice == "1":
            grocery_items.append("Butter")
        if choice == "2":
            grocery_items.append("Milk")
        if choice == "3":
            grocery_items.append("fruits")
        if choice == "4":
            grocery_items.append("coffee")

    else:
        print("0 to Exist,if not then,")
        print("Add items from the following available ones: ")

        # Iteration loop:
        # for item in instock_items:
        #     print("{0}. {1}".format(instock_items.index(item)+1,item))

        # enumerate() method:
        for num,item in enumerate(instock_items):
            print("{0}. {1}".format(num+1,item))

    choice = input()

print(grocery_items)

# If we are working with large data in list like 1 lack in the list or 10 lakh in the list
# The above iterating method is not a efficient one.
# The time complexity of above code will be O(n2) or O(nm)
# If we have 10lakh items  then 10lakh X 10Lakh will take more computing time.

# Enumerate() function in python
# print("{0}. {1}".format(instock_items.index(item)+1,item))
# The above line is not a efficient line of code. Essentially what it does is
# It goes into each of the character. It goes and checks the value of item
# Let us say the value of item is something called "Tea Bag". It goes to the first index
# That is the starting position of the list '0'--> It checks whether it is tea bag, Yes or No
# Then it goes to second index and checks yes or no
# It goes to third index and checks yes or no
# It goes to fourth index and checks yes or no
# and finally goes to the correct position
# If in case it goes to 'Curd' which is what we are looking at. Then the loop automatically breaks here
# Essentially it not a good practice because we have iterate the loop for each and every item which we see.
# We iterating upon the list of instock_items using for loop
# and again inside loop also we are iterating the instock_items
# This makes the code look not very efficient
# In order to fix this we are going to use the enumerate() method in python
# for num,item in enumerate(instock_items):
#     print("{0}. {1}".format(num+1,item))
# Essentially the for loop here is running on the item
# here item is essentially something called "Butter" or "Curd" or "Tea Bag"...
#  It involves all the items that we created in this list
# In the same loop we can track whatever item we have we are able to track the index of the item
# The number essentially works with 0,1,2,3...
# in the same loop we are able to handle both the index and the corresponding items together.
# How it is able to track the item here as "Butter" "Milk" "Curd" ...
# And here the num is of type 0,1,2,3...
# How does enumerate works?
string1 = "abcdefghijklmnopqrstuvwxyz"
for index,char in enumerate(string1):
    print(index + 1,char)


print(dir(enumerate))

for letter in enumerate(string1):
    print(letter)

# The above for loop provides the pair of values which contains the index and the value
# automatically it finds that the first value which we are providing on the loop is of index type or integer type.
# The second one is the actual value that is contained
# index value of each item is automatically taken care by the enumerate() method
# num --> is the index or index type.
# item --> value of the items in the list or value type.



