#第一题
def f(x):
    return 3*(x**4)-9*(x**2)+x/2

l=[54,96,83,64,234,158,364]

for x in l:
    print('f(%d)=%d' % (x,f(x)))

#第二题
def la(x):
    if 90<=x<=100:
        print('a')
    elif 80<=x<90:
        print('b')
    elif 60<=x<80:
        print('c')
    else:
        print('d')

x=int(input())
la(x)

#第三题
def la(x):
    l=[]
    for i in range(len(x)+1):
        if i % 2 == 1:
            l.append(x[i-1])
    print(l)

x = list(map(int,input().split()))
la(x)

#第四题
n=[1,2,3,4]
n2=[]
def la():
    for i in n:
        for j in n:
            for k in n:
                if i!=j and k!=j and i!=k:
                    n2.append(str(i)+str(j)+str(k))
    print('共有{}种组合，分别是{}'.format(len(n2),n2))
la()

#第五题
x=input('请输入第一个数:')
y=input('请输入第二个数:')
z=input('请输入第三个数:')
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)
