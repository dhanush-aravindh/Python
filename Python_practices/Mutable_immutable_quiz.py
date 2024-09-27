# 5. What is the output of the code below?
x = 'name = "Virat \bKohli"\nprint(name)'
exec(x)

x =" Your\'s truly \n Shreya"
print(x)

txt = "India \\ Australia \\ England \\ Bangladesh \\ WestIndies"
print(txt.replace("\\",",",2))

txt = "Flipkart\tBigbillion\tDays\tShop now "
l=txt.split(" ")
m=len(l)
n=txt.count(" ")
print(pow(m,n,5))

txt = "Japan \\ China \\ Singapore \\ London"
l=txt.split("\\")
print(l)
c=0
for i in l:
    if(i.find('a')!=-1):
        c+=1
print(c)

a = "1\\0\\1\\0\\0\\0\\1"
l=a.split("\\")
print(l)
print(any(l))


a = "a\\b\'c\\d\ne\\f"
x=a.split("\\")
print(x)
mi=1
for i in x:
    mi*=len(i)
print(mi)


a = "2\\3\\9\\4"
x=a.split("\\")
l=[]
for i in x:
    z=bin(int(i))
    l.append(z.replace("0b",""))
print("*".join(l))

s={1,True,1,"PrepInsta"}
l=[]
for i in s:
    l.append(str(i))
x="\\".join(l)
print(x)


s  = "Thankyou\tforbeingthere\nGratitude"
print(repr(s))

print()
txt = "Spinit\\ \b \rWinit"
print(txt)


s=r"Stack\\Queue\\Tree\\LinkedList"
print(s.count('\\'))

x="\tPrepInsta\tNew Channel\nNew Beginnings"
y=x.lstrip()
z=x.rstrip()
print(z.count(" ")+y.count(" "))




