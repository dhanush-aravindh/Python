# name = input("Enter your name:")
# age = int(input("Enter your age {0}: ".format(name)))
# print(age)
# Since we are entering age as a string we need to convert into integer variable so that we can enter the value of age
# as integer instead of string
# we can use int() function which is a in-built function in python what it does is it automatically converts string into
# integer datatype
# Make sure we enter only numeric values  and we don't enter like twenty one in words  since it will create
# lot of problems
# we want to create an interface to check his age is less than 18 years and also if he enters any negative number we
# need to check
# if age <= 0:
#     print("Enter the correct valid age")
# elif age < 18:
#     print("Sorry you're not old enough to vote come back in {0} years".format(18-age))
# elif age > 1000:
#     print("Sorry Thor you're a mystical character")
# elif age == 18:
#     print("Congratulations you can barely vote")
# else:
#     print("Congratulations you can vote")

# If and If ---> both the condition statements get executed
# If and elif---> The condition which is true will be executed and the other condition will not be executed
answer = 11
print("Let's play a game")
print("Guess a number between 1 to 20")

guess = int(input("Enter the number: "))
if guess < answer:
    print("Sorry, bad luck !! Please guess higher")
    print("No problem try again")
    guess = int(input())
    if guess == answer:
        print("Congrats you got it in the 2nd time")
    else:
        print("you guessed incorrectly again")
elif guess > answer:
    print("Sorry, bad luck !! Please guess lower ")
    guess = int(input())
    if guess == answer:
        print("Congrats you got it in the 2nd time")
    else:
        print("you guessed incorrectly again")
else:
    print("Congratulations you guessed correctly")

# elif cannot be the first statement it is followed by if statement
# if the if condition is true , elif and else is not executed
# if is false, elif is True , if and else is not executed
# if is false, elif is false, else is executed
