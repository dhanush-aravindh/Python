
# a=[]
# for i in range(100,1000):
#     a.append(i)
#     #print(a.index(a[-1]))
#     print(a[-1])
# counter = 0
# for i in a:
#     counter = counter + 1
#     print(counter)


a=[]
for i in range(100,1000):
      a.append(i)
print(a)
print(a.__len__())
print(len(a))

b = []
for i in range(1,101):
      if i % 2 == 0 :
            b.append(i)

print(b)
print(len(b))
