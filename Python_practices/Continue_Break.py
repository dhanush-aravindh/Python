shopping_items = ["eggs","apples","maggi","stale bananas","bread","curd"]

for item in shopping_items:
    if item != "stale bananas":
        print("{0} Added to cart".format(item))

print('*'*35)

# implementing with continue statement
for item in shopping_items:
    if item == "stale bananas":
        continue

    print("{0} Added to cart".format(item))

# How does the continue work?
# Continue tells the for loop for this part of the code/condition to skip the iteration
# we can debug the code and check how it works
# continue statement helps to skip the iteration
# All the other ones are then followed

# Learning break statement:
# Break statements are used to break the loop or flow of the statements
# Completely stopping the implementation of the loop
print("-"*35)
for item in shopping_items:
    if item == "stale bananas":
        break
    print("{0} added to the cart".format(item))

# finding the index of the shopping_item
item_find = "stale bananas"
found_index = None # It is similar to null in other languages
print(len(shopping_items))
for i in range(len(shopping_items)):
    if (shopping_items[i] == item_find):
        found_index = i
        break
print("The {} are found at position {}".format(item_find,found_index))
# Break statement only the breaks the for loop in which it is being used
# Breaks only the current loop in which it is contained
