#第一题
def f(*x):
    for i in x:
        y=3*i**4-9*i**2+i%2
        print(y)
f(54,96,83,64,234,158,364)

#第二题
def cj(x):
    y=90 <= x <= 100 or 80 <= x < 90 or 60 <= x < 80 or x < 60
    if x>=60:
        if 80 <= x < 90:
            print('B')
        elif 60 <= x < 80:
            print('C')
        else:
            print('A')
    else:
        print('D')
    return y
y=cj(85)

#第三题
def f(x):
    a=[]
    for i in range(len(x)):
        if i%2==0:
            a.append(x[i])
    return a
print(f([1,2,3,4,5,6,7]))

#第四题
i=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a!=b)and(b!=c)and(c!=a):
                i=i+1
                print(a,b,c)
print("一共有%d组"%(i))

#第五题
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
lis1=[x,y,z]                        
for i in lis1:
    if x>y:
      x,y=y,x
    if y>z:
      y,z=z,y
    if x>z:
      x,z=z,x    
print(x,y,z)

#第六题
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
n=int(input('n='))
if n % 2==1:      
    print(odd(n))   
else:
    print(even(n))

