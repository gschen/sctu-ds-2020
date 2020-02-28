#第一题
list=[54,96,83,64,234,158,364]
def f(x):
    return 3*x**4-9*x**2+x/2
for i in list:
    print(f(i))
#第二题

x=int(input('x='))
def chengji(x):
    if 90<=x<=100:
        print('A')
    elif 80<=x<90:
        print('B')
    elif 60<=x<80:
        print('C')
    elif x<60:
        print('D')
    return
print(chengji(x))
#第三题
list1=[]
def f(*x):
    for i in range(len(x)):
        if i%2==0:
            list1.append(x[i])
    return list1
print(f(1,2,3,4,5,6,7))
#第四题
list2=[1,2,3,4]
x=0
for a in list2:
    for b in list2:
        for c in list2:
            if a != b and a != c and b != c:
                x=x+1
                print(a*100+b*10+c)
print("能组成%d个"%(x))
#第五题
list=[1,3,2]
for x in list:
    for y in list:
        for z in list:
            if x<y and x<z and y<z:
                print(list.sort())
print(list)
#第六题
n=int(input())
def f(n):
    if n%2==0:
        sum1=0
        for i in range(2,n+1,2):
            sum1=sum1+1/i
            print(sum1)
    else:
        sum2=0
        for i in range(1,n+1,2):
            sum2=sum2+1/i     
            print(sum2)   
print(f(n))
#第七题：
def f(n):
    x,y,z,m=0,0,0,0
    for i in n:
        if i.isalpha():
            x+=1
        elif i.isdigit():
            y+=1
        elif i.isspace():
            z+=1
        else:
            m+=1
    print("%d,%d,%d,%d"%(x,y,z,m))
print(f(list(input().split(','))))


