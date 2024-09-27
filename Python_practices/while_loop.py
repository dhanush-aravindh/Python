limit = int(input("Enter the number: "))
i = 1
while i <= limit:
    if i % 5 == 0:
        i = i+1
        continue
    print("The value of i is {0}".format(i))
    #i = i+1
    i += 1

odd_numbers = [1,3,6,7,9]

for x in odd_numbers:
    if x % 2 == 0:
        print("The numbers are unacceptable")
        break

    else:
        print("The numbers are fine")
# else:
#     print("The numbers are fine")