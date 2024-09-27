# How python knows blocks and statements
# In Java , the block of code is represented using {}
# In python , We have Indentation which takes care about the block structure
# for i in range(1,11):
# print("No. {0:2} squared is {1:3} cubed is {2:4}".format(i,i**2,i**3))
# File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\Blocks_and_statements.py", line 5
#     print("No. {0:2} squared is {1:3} cubed is {2:4}".format(i,i**2,i**3))
#     ^
# IndentationError: expected an indented block after 'for' statement on line 4
for i in range(1,11):
    print("No. {0:2} squared is {1:3} cubed is {2:4}".format(i,i**2,i**3))
    print("-" * 35)

for i in range(1,11):
    print("No. {0:2} squared is {1:3} cubed is {2:4}".format(i,i**2,i**3))
print("-" * 35)


age1 = int(input("Enter your age: "))
if 18 <= age1 <= 100:
    print("You can vote")