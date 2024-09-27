even = [2,4,6,8,10,12,14]
odd = [1,3,5,7,9,11,13,15]

even.extend(odd)
print(even)
another_list = even
print(another_list)

even.sort()
print(even)

print()
print(another_list)

print(id(even))
print(id(another_list))