#1
def yxw(*x):
    for i in x:
        y=3*i**4-9*i**2+i/2
        print(y)
yxw(54,96,83,64,234,158,364)


#2
def yxw(n):
    if n>90 and n<100:
        return "A"
    if n>80:
        return "B"
    if n>60:
        return "C"
    if n<60:
        return "D"
n=int(input())
print(yxw(n))


#3
def yxw(*n):
    L=[]
    for i in n:
        a=n.index(i)
        if a%2 != 0:
            L.append(i)
    return L
print(yxw(1,2,3,4,5,6,7,8,9,0))


#4
L=[1,2,3,4]
s=0
for i in L:
    for j in L:
        for k in L:
            if i != j and i != k and j != k:
                s=s+1
                print("%d%d%d"%(i,j,k))
print(s)


#5
x=int(input())
y=int(input())
z=int(input())
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)


#6
def yxw(n):
    a=1
    s=0
    if n%2==0:
        b=2
        while b<=n:
            c=a/b
            b=b+2
            s=s+c
        print(s)
    else:
        b=1
        while b<=n:
            c=a/b
            b=b+2
            s=s+c 
        print(s)
n=int(input())
yxw(n)


#7
def yxw(n):
    a=0
    b=0
    c=0
    d=0
    for i in n:
        if i.isalpha():
            a=a+1
        if i.isdigit():
           b=b+1
        if i.isspace():
            c=c+1
        else:
            d=d+1
    print("字母:%d,数字:%d,空格:%d,其他:%d"%(a,b,c,d))
n=input()
yxw(n)