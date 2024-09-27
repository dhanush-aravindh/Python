print("Hello World")
# Print is a function in Python like printf or scanf in C .
# Hello World is the argument we are passing inside the function
# we can also use any type of argument inside print function
print(1+2)
print(10*3)
print()  # It creates empty space in the output console Empty print function creates empty space
print("PrepInsta", "is", "the", "best", 5)
# print("is")
# print("Best")
# Swig lines indicate types and warning , Green lines - minor warning , Yellow lines-Strong warning ,
# Red lines - Error

print(10*3.5)
# Precision in python and how to enforce them
# Print is a function

# Separator:
print("PrepInsta", "is", "the", "best", sep='_')
print("PrepInsta", "is", "the", "best", sep="__@__")
print("PrepInsta", "is", "the", "best", sep='')

# Default separator is ' '
print("PrepInsta", "is", "the", "best", sep=' ')
print("PrepInsta", "is", "the", "best")

# End: We can use any character,number or symbol to append at the end of each sequence beinging executed by print() function
print("PrepInsta", "is", "the", "best", end='@@ ')
print("Next line")

print("PrepInsta", "is", "the", "best", end='\n')
print("Next line")

print("PrepInsta", "is", "the", "best", end='@@\n')
print("Next line")



# \n is a escape sequence which is used to print new line after execution of the print statement
# whereas other characters append each and every sequences after excution of one print function