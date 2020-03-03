#1
def f(*x):
    for i in x:
        s=3*i**4-9*i**2+i/2
        print(s)
f(54,96,83,64,234,158,364)


#2
x=eval(input("请输入成绩："))
def f(x):
    if 90<=x<=100:
        print("A")
    elif 80<=x<=90:
        print("B")
    elif 60<=x<=80:
        print("C")
    else:
        print("D")
    return x    
print(f(x))

#3
def f(x):
    li1=[]
    for i in range(len(x)):
        if i%2==1:
            li1.append(x[i])
    return li1
print(f([1,2,3,4,5,6,7]))

#4
n=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a!=b)and(b!=c)and(c!=a):
                n=n+1
                print(a,b,c)
print("一共有%d组"%(n))


#5
x = int(input('第一个整数：'))
y = int(input('第二个整数：'))
z = int(input('第三个整数：'))
lis1=[]
lis1.append(x)
lis1.append(y)
lis1.append(z)                        
for i in lis1:
    if x>y:
      x,y=y,x
    if y>z:
      y,z=z,y
    if x>z:
      x,z=z,x    
print(x,y,z)


#6
def odd(n):   
    s=0
    for i in range(1,n+1,2):        
        s=s+1/i    
    return s
def even(n):    
    s=0    
    for i in range(2,n+1,2):        
        s=s+1/i        
    return s
n=int(input("请输入一个数："))
if n % 2==1:      
    print(odd(n))   
else:
    print(even(n))

#7
s=input('输入一行字符:\n')
a=0
b=0
c=0
d=0
for m in s:
    if m.isalpha():
        a+=1
    elif m.isspace():
        b+=1
    elif m.isdigit():
        c+=1
    else:
        d+=1
print('英文=%d,空格=%d,数字=%d,其他字符=%d'%(a,b,c,d))