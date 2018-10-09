print("Hello") #megjegyzes
'''
tobb soros
megjegyzes
'''
a = 2**3#hatvanyozas
b = 1.2
print(b)
c = 2 + 3j
print (type(a))#tipuslekerdezes
print (type(b))
print (type(c))
d=2 // 3#egesz osztas
e=2 % 3#maradek
s="abc"
r="12"
print (s+r)
print (20*s+r)
type(s) is str #logikai
print("a = ", a)
print("a = ", a, sep="",end="\n")
print("%d, %d" % (a, d))
for i in range(2, 10, 2):
    print(i)
for i in range(15, 10, -1):
    print(i)
g = "abcd1234"
print(g[2:8:2])#string kiiras
print(g[-1])#utolso elem
print(g[len(g)-1])#string hossza
print(g[::-1])
print(g.upper())#uj stringet hoz letre
print(g.lower())
print(g.replace("23", "00"))#csere
if a==8:
    print("Az a erteke 10")
else: print("Az a erteke nem 10")

str="kk"
str0=str.lower().replace(" ","")
str1=str[::-1]




if str0==str1:
    print("igen")
else: print("nem")
    

