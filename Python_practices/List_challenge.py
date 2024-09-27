digits = list("342691652")
print(digits)

# int_list = [int(i) for i in digits]
# print(int_list)

# int_list = []
# for i in digits:
#     int_list.append(int(i))
# print(int_list)

# digits = list("342691652")
int_list = []
index = 0

while index < len(digits):
    int_list.append(int(digits[index]))
    index += 1

print(int_list)
