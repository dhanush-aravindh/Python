fruits = [
          "Apple",
          "Bananas",
          "Orange",
          "Mangoes",
          "Litchi",
          "Water Melon",
          
          ]

for fruit in fruits:
    print(fruit)

# Join method work upon a string
# We are adding ", " for each of the iterations of the fruit
# Basically join word also on the right hand of the object that we have passed
# It would iterate upon it automatically
# It works as a kind of for loop for us.
# we can write specific conditions if we want within the join methods
# simply tell the values that these are values into which we need to iterate upon
# join function only work upon on strings
separator = " + "
value = separator.join(fruits)
print(value)
# "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\venv\Dhanush\Python\Scripts\python.exe" "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\venv\Join_method.py"
# Traceback (most recent call last):
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\venv\Join_method.py", line 23, in <module>
# value = separator.join(fruits)
# ^^^^^^^^^^^^^^^^^^^^^^
# TypeError: sequence item 6: expected str instance, int found
