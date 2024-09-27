for x in range(1,5):
    print("We are in iteration {} of for loop".format(x))
else:
    print("Now, we are in the else block of the loop")

print("Came out of both for and its else loop")

# If the for loop condition is satisfied from starting condition to end condition
# and executed successfully
# The else part will be then executed successfully when all the for loop condition is satisfied
i = 1
while i < 5:
    print("We are in iteration {} of for loop".format(i))
    i = i + 1
else:
    print("Now, we are in the else block of the loop")

print("Came out of both for and its else loop")

# In what cases the else loop fails:
odd_numbers = [1,3,6,7,9]

for x in odd_numbers:
    if x % 2 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("The numbers are fine")

# we think that break statment  is implemented then we should go to else
# However it is opposite if the break statement is not executed we go to else.


odd_numbers = [1, 3, 5, 7, 9]

index = 0
while index < len(odd_numbers):
    x = odd_numbers[index]
    if x % 2 == 0:
        print("The numbers are unacceptable")
        break
    index += 1
else:
    print("The numbers are fine")