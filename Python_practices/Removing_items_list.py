
# grocery_items = []
instock_items = ["Milk",
                 "Curd",
                 "Rice",
                 "Bread",
                 "Coffee",
                 "Butter",
                 "Tea Bag"
                 ]
choice = "_"
grocery_items = []

# The below list valid_choice is used to carry the index values of the items in
# the instock_items
# list comprehension method:
# valid_choice = [str(i) for i in range(1,len(instock_items) + 1)]
# print(valid_choice)
valid_choice = []
for i in range(1,len(instock_items)+1):
    valid_choice.append(str(i))

print(valid_choice)
print()

# Butter Butter. We need to avoid repetation of Item
# We want to remove the item in which it was added earlier
# we have to create a index so that we can add particular items in the index

# Deleting and removing in python is very very different from C or C++
while choice != "0":
    if choice in "12345":
        #print("Adding {0} to BigBasket Cart".format(choice))
        index = int(choice) - 1 # 1-1 = [0], 4-1= [3]
        chosen_item = instock_items[index] # index value is 3
        #grocery_items.append(chosen_item) # Value entered will be bread
        if chosen_item in grocery_items:
            print("Item {0} removed from List".format(chosen_item))
            grocery_items.remove(chosen_item)
        else:
            grocery_items.append(chosen_item)
            print("Item {0} added to the list".format(chosen_item))
        print("Your cart now contains: {}".format(grocery_items))

        # The below code in not a proper way according to industry standards
        # There are list comprehensions which will be best for implementing to solve this problem
        # We should know all the different ways to implement
        # if choice == "1":
        #     grocery_items.append("Butter")
        # if choice == "2":
        #     grocery_items.append("Milk")
        # if choice == "3":
        #     grocery_items.append("fruits")
        # if choice == "4":
        #     grocery_items.append("coffee")

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

