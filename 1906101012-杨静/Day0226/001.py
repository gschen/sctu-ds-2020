习题1
list1=[54,96,83,64,234,158,364]
for x in list1:
    def f(x):
        return 3*x**4-9*x**2+x/2
print(f(x))

习题2
grade = int(input("请输入你的成绩:"))
def grade(x):
    for x in range(1,101)
if x >= 90 and x <= 100:
    return 'A'
if x >= 80 and x < 90:
    return 'B'
if x >= 60 and x < 80:
    return 'C'
else:
    return 'D'
print(grade(x))

习题3
list0=[]
def an(x):
    for y in range(len(x)):
        if y % 2 == 0:
            list0.append(x[y])
    return list0
ret = an([1,2,3,4,5,6,7])
print(ret)

练习4
x=0
for y in range(1,5):
    for z in range(1,5):
        for h in range(1,5):
            if y!=z  and z!=h and h!=y:
                x+=1
                print(y,z,h)

练习5
x,y,z=map(int,input('请输入x,y,z:').split())
if x>y>z:
    print(z,y,x)
elif x>z>y:
    print(y,z,x)
elif y>x>z:
    print(z,x,y)
elif y>z>x:
    print(x,z,y)
elif z>x>y:
    print(y,x,z)
else:
    print(x,y,z)

练习6
x=int('请输入一个数：')
def asd(x):
    sum=0
    if x==1:
        return 1/1
    elif n==2:
        return 1/2
    else:
        return 1/x+asd(x-2)
print('函数求和结果为：',asd(x))

练习7
a,b,c,d=0,0,0,0
str=input()
def yang(str,a,b,c,d):
    for y in str:
        if x.isapha():
              a+=1
        elif x.isdigit():
              b+=1
        elif x.isspace():
              c+=1
        else:
              d+=1
    return a,b,c,d
print(yang(str,a,b,c,d))