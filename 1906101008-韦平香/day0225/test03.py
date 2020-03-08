#def Aplus(a,b):
 #   return a+b
#result=Aplus(1,2)
#print(result)
#print(Aplus(10,12))

#def dir{r}:
#return r**2*3.14
#print(dir(s))

#def circle(r,pi):
    area=r**2*pi

    return area
circle(3,3.14)
print(area)

print(dircle(6,3.14))
print(dircle(pi=3.14,r=6))

a=2
def main():
    b=3
    print(a)
main()
print(b)

circle=lambda r,pi:r**2*pi
print(circle(3,3.14))

def change(a):
    a=10

b=2
change(b)#2=>a,a=2=>a=10
print(b)

c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

b='123'
b=123

def main(x,*y):
    print(x)
    for i in y:
        print(y)

main(1,11,12,13,14)