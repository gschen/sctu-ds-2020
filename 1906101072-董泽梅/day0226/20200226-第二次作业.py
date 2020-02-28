#第一题
def first(x):
    y=3*x**4-9*x**2+x/2
    return y
l=[54,96,83,64,234,158,364]
for i in l:
    s=first(i)
    print(s)

#第二题
score= int(input('请输入分数：'))
def second(score):
    if score >=90:
        print('A')
    elif 90> score >=80:
        print('B')
    elif 80> score >=60:
        print('C')
    elif score <=60:
        print('D')
second(score)

#第三题
def thirth(p):
    li=[]
    for i in range(len(p)):
        if i % 2 == 0:
            li.append(p[i])
        else:
            pass
    return li
l=[1,2,3,4,5,6,7,]
r=thirth(l)
print(r)

#第四题
sum=0
for i in range(1,5):
    for j in range(1,5):
        if i!=j:
            continue
        else:
            for k in range(1,5):
                if k==i or k==j:
                    continue
                else:
                    print(str(i)+str(j)+str(k),end=' ')
                    sum=sum+1
print('')
print('总计有'+str(sum)+'个数')

#第五题
x=int(input('请输入一个整数：'))
y=int(input('请输入一个整数：'))
z=int(input('请输入一个整数：'))
if x>y>z:
    print(z,y,x)
elif x>z>y:
    print(y,z,x)
elif z>x>y:
    print(y,x,z)
elif z>y>x:
    print(x,y,z)
elif y>x>z:
    print(z,x,y)
elif y>z>x:
    print(x,z,y)

