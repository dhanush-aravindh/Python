# import module
#
# print(module.addition())

import module
print(module.addition(5,7))
print(module.subtraction(8,1))
print(module.multiplication(10,5))
print(module.division(6,4))

from module import addition
print(addition(5,6))

from module import subtraction
print(subtraction(6,7))

from module import multiplication
print(multiplication(6,7))

from module import division
print(division(8,3))