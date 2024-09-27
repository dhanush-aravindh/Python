# Weight = 70
# print("My Weight is:" + Weight + "Kgs")
# Traceback (most recent call last):
#   File "C:\Users\HP\IdeaProjects\PrepInsta Prime Python\String_replacement_fields.py", line 2, in <module>
#     print("My Weight is:" + Weight + "Kgs")
#           ~~~~~~~~~~~~~~~~^~~~~~~~
# TypeError: can only concatenate str (not "int") to str


Weight = 70
print("My Weight is:" + str(Weight) + " Kgs")
# str() function converts integer to string

print("My weight is {0} kgs".format(Weight))
# It is like using %d is C
# printf("%d,%d",x,y)
# And in C++ : cout<<x<<y<<:""
# It parallel to C and C++

print("We have {0} days in {1},{2},{3},{4},{5},{6},{7}"
      .format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))
# The first input we have to take is  marked by zero {0} and second input is marked by {1} and goes on.
# The inputs can neither be integer or string as well
# Based on the order of occurance in format() values will be printed
# We can have multiple string replacement fields in a single print or single line of code
# It reduces our coding time also

print("We have {0} days in Jan,Mar,May,Jul,Aug,Oct,Dec"
      .format(31))
print()
print("Jan:{2},Feb:{0},Mar:{2},Apr:{1},May:{2},Jun:{1},Jul:{2},Aug:{2},Sep:{1},Oct:{2},Nov:{1},Dec:{2}"
      .format(28,30,31))
print()
print("Jan:{2},Feb:{0},Mar:{2},Apr:{1},May:{2},Jun:{1},Jul:{2},Aug:{2},Sep:{1},Oct:{2},Nov:{1},Dec:{2}"
      .format(28,"30 Days",31))
print()

print("""Jan:{2},
Feb:{0},
Mar:{2},
Apr:{1},
May:{2},
Jun:{1},
Jul:{2},
Aug:{2},
Sep:{1},
Oct:{2},
Nov:{1},
Dec:{2}""".format(28,30,31))

# String formating: