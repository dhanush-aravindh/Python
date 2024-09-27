# Index      0                        25
alphabets = "abcdefghijklmnopqrstuvwxyz"
# Neg index -26                      -1
print(len(alphabets))
print(alphabets)
# Forward Slicing
print(alphabets[0:26])
print(alphabets[0:25])
# Step Slicing
print(alphabets[0::2])
# Backward slicing
# It is possible because we are changing the direction by reversing the index values
# and also by reversing the  step values
# Backward slicing is possible only with the negative step slicing is present and the step value should be negative.
print(alphabets[25:0:-1])
print(alphabets[25::-1])
print(alphabets[0:25:-1]) # Not possible
print(alphabets[25:0]) # Not possible
print(alphabets[25:-1:-1])
# Not possible
# because we have represented the same value as both start and end value in the slicing so no values is printed
print(alphabets[-26::1]) # Forward Slicing
print(alphabets[-1::-1]) # Backward Slicing
print(alphabets[5::-1])
print(alphabets[-1:0:-1])

# mno
print(alphabets.index('m'))
# mno
print(alphabets[12:15]) # mno
print(alphabets[-14:-11]) # mno
print()
# onm
print(alphabets[14:11:-1]) #onm
print(alphabets[-12:-15:-1]) #onm
print(alphabets[-12:11:-1])
print(alphabets[14:-15:-1])
print()
# ehkm
print(alphabets[4:14:3]) # ehkn
print(alphabets[-22:-12:3]) #ehkn
print(alphabets[-22:-10:3])# ehkn
print()
# nkhe
print(alphabets[13:3:-3]) # nkhe
print(alphabets[-13:-23:-3]) #nkhe
print(alphabets[13:-23:-3])
print()

# Alphabets:
print(alphabets[0:8]) # abcdefgh
print(alphabets[:8])
print(alphabets[-26:8])
print(alphabets[-26:-18]) # abcdefgh
print()
# last 20 characters in backward slicing
print(alphabets[-1:-21:-1]) # zyxwvutsrqponmlkjihg
print(len(alphabets[-1:-21:-1])) # 20
print(alphabets[25:5:-1])
print()
# first 20 characters
print(alphabets[0:20])
print(alphabets[:20])
print(alphabets[-26:-6])
print(alphabets[-7::-1])
print()

# checking the length
print(len(alphabets))
print(len(alphabets[0:20]))


d={'a':5,'b':3,'c':2}
s=""
for i in d.keys():
    s+=i*d[i]
print(s[3::-2]) # " aa " will be printed
print(d.keys())
print(s)


variable= "Preparation in PrepInsta"
print(variable[23:0:-1])

print(range(10))
s="malayalam"
r=s[::2][::-1]
print(r)

n1 = ['chocolate', 'biscuit', 'icecream']
n2 = [n.title() for n in n1]
print(n2[2][0])
print(n2)

l=[3,5,7,9]
l.append([1,2,3,4])
print(len(l[2:]))
print(l)

l=[3,4,3,1,2,3,7,1,7,5]
z=sorted(l,key=l.count,reverse=True)
print(z[1:4])
print(z)

def take_second(e):
    return e[1]
l = [(2, 2), (3, 4), (4, 1), (1, 3)]
sl = sorted(l, key=take_second)
print(sl[3][1])
print(sl)

l=["abab","bbbbb","cbbbbab"]
nl=[]
for i in l:
    nl.extend(i.split("b"))
s=list(set(nl))
print(s[1:])
print(s)
print(nl)

l=["a","b","c"]
z=l*2
print(z[1:2])
print(z)

l=['x','y','z']
s=""
for i in l:
    s+=i*((l.index(i)+1)**2)
print(s[3:6:2])
print(s)

s="abababacacadc"
x=list(s)
z=sorted(x,key=x.count,reverse=True)
print(z[3:7])
print(z)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = tuple(zip(a, b))
print(x)
print(x[2][1])

l1 = ["eat","sleep","repeat"]
a=(list(enumerate(l1)))
print(a)
print(a[1:2])

numbers= "1,273,456,546,785,554"
print(numbers[1::4])

string1= "Prepinsta Prime"
print(string1[9-13])

string1= "Preparation in Prepinsta"
print(string1[23::-3])

string1= "abcdefghijklmnopqrstuvwxyz"
print(string1[14::-3])





