
#1
def f(*x):
    for i in x:
        s=3*i**4-9*i**2+i/2
        print(s)
f(54,96,83,64,234,158,364)



#2
n=int(input('请输入一个正整数：'))
def grade(n):
    if n <=100 and n >90:
        print('A')
    elif n <=90 and n > 80:
        print('B')
    elif n <=80 and n > 60:
        print('C')
    else:
        print('D')
grade(n)



#3
def lz(q):
    listl=[]
    for i in range(len(q)):
        if i % 2 == 0:
            listl.append(q[i])
        else:
            pass
    return listl
l=[1,2,3,4,5,6,7]
s=lz(l)
print(s)


#4
sum=0
for i in range(1,5):
    for j in range(1,5):
        if i==j:
            continue
        else:
            for l in range(1,5):
                if l==i or l==j:
                    continue
                else:
                    print(str(i)+str(j)+str(l),end=' ')
                    sum=sum+1
print('')
print('总计有'+str(sum)+'个数')


#5
x = int(input('请输入第一个整数：'))
y = int(input('请输入第二个整数：'))
z = int(input('请输入第三个整数：'))
if x >  y > z:
    print(z, y, x)
elif x > z > y:
    print(y, z, x)
elif y > x > z:
    print(z, x, y)
elif y > z > x:
    print(x, z, y)
elif z > x > y:
    print(y, x, z)
else:
    print(x, y, z)