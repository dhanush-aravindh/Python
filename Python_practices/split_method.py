paragraph = "PrepInsta Python course is a good way for us to learn python"

word = paragraph.split()
print(word)
# Split method converts the entire/any string into a list
# Whenever there is a empty space between the words in the string it converts it into new element in the list

numbers ="9,123,571,719,819,182"
print(numbers.split(","))

# Split is opposite of join
# Joining different list together and split is splitting that paragraph/string into list

indiv_list = ['9','1','2',
              '3','5','7',
              '1','7','1',
              ]
values = " ".join(indiv_list)
print(values)

final_values = values.split()
print(final_values)
#the default split value is empty space

indiv_list = ['9','1','2'," ",
              '3','5','7'," ",
              '1','7','1'," ",
              ]


values = "".join(indiv_list)
print(values)

final_values = values.split()
print(final_values)

indiv_list = ['9','1','2',
              '3','5','7',
              '1','7','1',
              ]


values = "".join(indiv_list)
print(values)

final_values = values.split()
print(final_values)

print(300000-15)