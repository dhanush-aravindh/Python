#          0 1 2   3   4   5   6   7    8   9  10   11   12
numbers = [3,7,200,201,203,214,281,300,301,302,309,40001,40009]

# del numbers[0:2]
# print(numbers)
#
# # When we delete the numbers from the List the index of the numbers present in the list is shifted.
# del numbers[9:]
# print(numbers)

min_allowed  = 200
max_allowed  = 400

# The best/Experienced programer writes the code in the below given way:
# The value of len() starts from 1
# The index value starts from 0
# The below code will work if the listed is sorted
start =0 #           (13-1=12     ),negative step slicing
for index  in range(len(numbers)-1,-1,-1):

    # print(numbers[index],index)
    if numbers[index] <=max_allowed: # 309 <=400 True
        start = index + 1
        break

    if numbers[index] <= min_allowed:
        start = index+1
        break

print(start)
del numbers[11:]
print(numbers)















# first: we create a stop variable
# Second: Store the index of the min_allowed in stop
# Third: Remove the elements from index zero to stop
# Fourth: We can twik the same to max_allowed
# The below code is return by the average programer:
# stop = 0
# for index,value in enumerate(numbers):
#     # if value >= min_allowed:
#     #     stop = index
#     #     break
#     if value >= max_allowed:
#         stop = index
#         break
#
# #del numbers[:stop] # min_allowed
# del numbers[stop:] # max_allowed
# print(numbers)



# for index ,value in enumerate(numbers):
#     #print("The value: {0:5} at index {1:2}".format(value,index))
#     if (value < min_allowed) or (value > max_allowed):
#         del numbers[index] # 6
#         #index = index-1 # 5
#     # But the for loop increments the index value to 7.
# print(numbers)

#  0  1    2    3     4    5   6    7    8    9    10
# [7, 200, 201, 203, 214, 281, 300, 301, 302, 309, 40009]
# why we are not able to get the correct answer is there is shift in the values
# Index of the values are changed.
# The value 3 is deleted and the value 7 is shifted to the index position of 3
# The same problem is faced by the number 40009 also
# As 40001 is deleted the value 40009 has shifted to this position
# The problem we are solving is applicable only to the list which is already sorted
# We are going to learn some tricks helpful for building coding logics specifically for python
# Step one : the list has to be sorted either in ascending or descending order
# if the list is descending we have to change the program little bit
# first we are going to delete the lower variable 3 and 7 based on min_allowed value

numbers = [3, 7, 200, 201, 203, 214, 281, 300, 301, 302, 309, 40001, 40009]
max_allowed = 400
min_allowed = 200

filtered_numbers = []

for num in numbers:
    if min_allowed <= num <= max_allowed:
        filtered_numbers.append(num)

print(filtered_numbers)

numbers = [3, 7, 200, 201, 203, 214, 281, 300, 301, 302, 309, 40001, 40009]
max_allowed = 400
min_allowed = 200

for i in range(len(numbers) - 1, -1, -1):
    if not (min_allowed <= numbers[i] <= max_allowed):
        del numbers[i]

print(numbers)
