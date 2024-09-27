import math
x = abs(3+5j)
print(x)
print(math.ceil(x))
# math.ceil --> it rounds up the value to nearest integer,
# The math. ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.
# abs()--> The Python abs() function return the absolute value.
# The absolute value of any number is always positive it removes the negative sign of a number in Python
# It also provides the magnitude of complex number
# which is calculated by |z| = squareroot(3^2+5^2)
import math
x=complex('3+5j')
y=complex('4+j')
z=abs(complex(x*y)) # 7+23j --> abs(7+23j)
# formula for complex multiplication: = (a+bi)(c+di) => (ac-bd)+(ad+bc)i
a = abs(7+23j)
print(a)
print(x,y)
print(z)
print(math.floor(z))
# Math.floor-->The math. floor() method rounds a number DOWN to the nearest integer,
# if necessary, and returns the result. Tip: To round a number UP to the nearest integer, look at the math. ceil() method

mydict = {0 : "Chocolate", 1 : "Factory"}
x = all(mydict)
print(x)
# The all() function returns True if all items in an iterable are true, otherwise it returns False.In case of dictionaries it checks keys.

mytuple = (0, 1, False)
x = any(mytuple)
print(x)
# any-->Return True if any element of the iterable is true. If the iterable is empty, return False.

x = bin(36)
print(x)
print(x.replace("0b",""))
#Explanation
#bin() returns binary value of given integer with \"0b\" prefix

exp="5%2+3*7"
print(eval(exp))
# The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
# eval() function used to evaluate infix expression.


x = 'name = "PrepInsta"\nprint(name)'
exec(x) # The exec() function executes the specified Python code.

x=58
y=bin(x)
z=y.replace("0b","")
print(z)
print(z.count('0')*z.count('1'))
# number of 0\'s in binary of 58(111010) is 2
#
# number of 1\'s in binary of 58(111010) is 4
#
# so answer is 2*4=8

mylist =iter( ["Bumrah", "Virat", "Hardik"])
x = next(mylist)
print(x)
# Next() gives the next iterator in given list
# Next() method cannot work without iter method

# The function pow(x,y,z) is evaluated as (x**y)% z

# print(chr(‘97’))
# print(chr(97))
# Explanation
# i) error (as it will consider '97' as a string instead of integer)
#
# ii) a (character on index 97)

# What is the output of function complex()?
print(complex()) #0j

#The function divmod(a,b), where both ‘a’ and ‘b’ are integers is evaluated as:
print(divmod(4,2)) # divmod(a,b) = (a//b, a%b)

print(list(enumerate([4,3])))

# Which of the following functions doesn’t accept lists as arguments?
# abs() takes two parameters and returns absolute difference between them

x = [1,2,3,6]
print(x[0:4:2])

x = [1,2,3,6]
y=slice(0,4,2)
print(x[y])

#print(slice(x,[0:4:2]))

x = 'list=[1,3]\nprint(list)'
exec(x)

#" print(slice(x,[0:4:2])) " will give an error. As x is not defined


l=[98,97,101]
print(pow(l[0],l[1],l[2]))

z= (98**97)
print(z % 101)

import math
l=[31.7811,36.9127,38.4041]
s=0
for i in l:
    s+=round(i,2)
print(math.floor(s))


x=hex(38)
print(x)

x=133
y=bin(x)
z=y.replace("0b","")
m=divmod(z.count('0'),z.count('1'))
print(m)


x='13%4*11*19-16*2'
y=x.replace("*","+")
print(eval(y))

x='5*6*7*8-9+11*13'
z=set(x)
y=x.replace("*","+")
print(eval(y)-len(z))
print(z)
print(eval(y))

l=['97//3','23*5%7']
s=0
for i in l:
    s+=eval(i)
print(s)
print(eval('97//3'))
print(eval('23*5%7'))
print(l)

x = format(128, 'b')
print(any(x))

x = 101
y=109
a=x^y
m=format(a,'b')
n=divmod(m.count("1"),m.count("0"))
print(n)

x=bin(138)
y=x.replace("0b","")
z=format(138,"b")
if(y==z):
    print(len(set(y+z)))
else:
    print(len(list(y+z)))


x = isinstance("PrepInsta", (float, int, str, list, dict, tuple))
y=isinstance(5,str)
z=isinstance([1,2,3],list)
l=[]
l.extend([x,y,z])
print(all(l))








