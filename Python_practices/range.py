# for i in range(1,21):
#     print("i is:{0:2}".format(i))
#
# print("===========================")
# #for j in range(1,21):
# #for j in range(20,0,-1): reversed the iteration
# for j in range(20,0,-3): # step slicing
#
#     print("Square of {0:2} is:{1:3}".format(j,j**2))



# like step slicing we can also use step value in the range() function

# Nested for loop:
# Print the tables for numbers from 1 to 20 till 10:
print("---Tables----")
for i in range(1,6):
    for j in range(1,11):
        print("{0:2} X {1:2} = {2:2}".format(i,j,i*j))
    print('-------------')

