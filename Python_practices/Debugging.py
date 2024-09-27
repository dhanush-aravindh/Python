# Debugger is used to check  where our code is breaking and widely used in Large scale applications for programers
# to understand what they are doing wrong and what are happening in different break points
# For example if our application requires name and age, and it is transferred from Database over the internet we want to
# know what has been taken as the input till the particular line , what variables are used and what values are used
# While working in an android application probably due to slow internet the variable such as name and age coming from
# database which is stored somewhere in the internet in the database are not received by our android application
# Somehow we are stopping in a particular line and know that the code is breaking and the app is crashing because we are
# unable to fetch the variable data, and we are unable to print the required output
name = input("Enter your name:")
age = int(input("Enter your age {0}: ".format(name)))
print(age)
if age <= 0:
    print("Enter the correct valid age")
elif age < 18:
    print("Sorry you're not old enough to vote come back in {0} years".format(18-age))
elif age > 1000:
    print("Sorry Thor you're a mystical character")
elif age == 18:
    print("Congratulations you can barely vote")
else:
    print("Congratulations you can vote")
# For example if we want to stop in line number 12 we can double-click on the line along the border we get a red line
# or red dot . We can also remove it by clicking on the red dot again
# Since we are working in the virtual machine we get a build number and process number which keeps changing as they
# indicate process carried out by virtual machines which the virtual machines carry out internally
# Once we enter the required variable values in debugger mode it shifts to new tab in the debugger mode
# Evaluate expression tab: we can test the values of the variables used by various condition and check the value is
# valid or invalid
# While in large file we want to know where ever by code has stopped and where am I
# Show execution point: The current point where the program execution has stopped
# Step over: It goes to the next line from show execution point with indentation
# To understand what kind of code is running we require a break point, how code is running, what kind of variable are
# there and what values the variables are having
# Ctrl + / is used for commenting the block of code
