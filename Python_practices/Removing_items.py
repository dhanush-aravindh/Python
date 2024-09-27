# Removing items from Unsorted List
# numbers = [301,391,7,202,40001,320,1,315,364]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
#
# min_allowed = 200
# max_allowed = 400
# filtered_numbers = []
#
# for num in numbers:
#     if min_allowed <= num <= max_allowed:
#         filtered_numbers.append(num)
# print(filtered_numbers)
# filtered_sort = sorted(filtered_numbers)
# print(filtered_sort)
#
# for i in range(len(numbers)-1,-1,-1):
#     if not (min_allowed <= numbers[i] <= max_allowed):
#         del numbers[i]
# print(numbers)
#
# i = 0
# while i in range(len(numbers)-1,-1,-1):
#     if not(min_allowed <= numbers[i] <= max_allowed):
#         del numbers[i]
#     i=i+1
#
# print(numbers)
# #
# # Removing of elements from unsorted list:
numbers = [301,391,7,11,202,40001,320,1,315,364]
min_allowed = 200
max_allowed = 400

# # If we are accessing the values in the reverse direction can help us to fix the proble,
# # Because accessing value in the reverse direction doesn't want the values necessarily wanted to be removed to be skipped.
# # So that we can access all the values of the list and helps to know the values to be deleted easily
#
# for index in range(len(numbers)-1,-1,-1):
#     if numbers[index] < min_allowed or numbers[index] > max_allowed:
#         print(index,numbers)
#         del numbers[index]

# top_index = len(numbers)-1
# for index,value in enumerate(reversed(numbers)):
#     #print(index,value) # Used to check whether the list is reveresed
#     # print(top_index-index,value) # Used to check whether the index is reversed
#     if value < min_allowed  or value > max_allowed:
#         print(top_index-index,value)
#         print("{0} is deleted from List".format(numbers[top_index-index]))
#         del numbers[top_index-index]
#
# print(numbers)

index = len(numbers)-1
#while index in range(len(numbers)-1,-1,-1):
     # if numbers[index] < min_allowed or numbers[index] > max_allowed:
     #     print(index,numbers[index])
     #     del numbers[index]
     # index+=1
while index >= 0:
  if numbers[index] < min_allowed or numbers[index] > max_allowed:
    print(index, numbers[index])
    del numbers[index]
  index -= 1
print(numbers)
