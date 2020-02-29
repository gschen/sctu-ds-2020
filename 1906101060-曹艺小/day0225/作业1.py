#第一题
def f(*x):
    for i in x:
        a=3*i**4-9*i**2+i/2
        print(a)
f(54,96,83,64,234,158,364)
#第二题
x = int(input("请输入成绩："))
def main(x):
    if 90 <= x < 100:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 60 <= x < 80:
        return 'C'
    else:
        return 'D'
print(main(x))
print(x=85)
#第三题
def hs(*x):
    lis1=[]
    a=len(x)
    for i in range(0,a,2):
        lis1.append(x[i])
    print(lis1)
hs(1,2,3,4,5,6,7)
#第四题
count=0
for i in range(1,5):
    for s in range(1,5):
        for l in range(1,5):
            if (i!=s) and (i!=l) and (s!=l):
                count=count+1
                print(str(i)+str(s)+str(s),end=' ')
print(' ')
print('最终的结果为：%s个'%count)
#第五题
x,y,z=map(int,input("输入三个整数：").split(','))
if x>y:
    x,y=y,x
if x>z：
    x,z=z.x
if y>z:
    y,z=z,y
print(x,y,z)
#选做 第六题
x=int(input("请输入x:"))
def hs(x):
    sum=0
    if x % 2==0:
        for i in range(2,x+1,2):
            a=1/b
            sum=sum+b
        return sum
    else:
        for a in range(1,n+1,2):
            b=1/a
            sum=sum+b
        return sum
 print(hs(x))
