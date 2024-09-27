empty = [] #1
odd = [1,3,5,7] #2
even=[2,4,6,8]

numbers = odd+even #3
print(numbers)

sorted_numbers = sorted(numbers) #4
print(sorted_numbers)

digits = list("3553662") #5
print(digits)

slice = numbers[4:] #6
print(slice)

new_numbers = numbers.copy()
print(new_numbers)

print(numbers is new_numbers) # It checks whether both the list are same
print(id(numbers),id(new_numbers))

print(numbers == new_numbers)

instock_items = ["Butter",
                 "Bread",
                 "Cream",
                 "Milk",
                 "Curd",
                 ]
print(instock_items)

instock_items[4] = "Coffee"
print(instock_items)

print(instock_items[2:])

#instock_items[2:] = "Unavailable" # replaced by the contents of the iterable t

instock_items[2:] = ["Unavailable","Unavailable","Unavailable"]
print(instock_items)





