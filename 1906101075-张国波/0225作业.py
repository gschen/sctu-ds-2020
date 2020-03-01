1、
i = [54,96,83,64,234,158,364]
def f(x):
    zhi = 3*x**4-9*x**2+x/2
    return zhi
for x in i:
    print(f(x))



2、
y = int(input('请输入成绩:'))
def judge(y):
    if y>=90:
        return ('你的成绩等级为A')
    elif y>=80:
       return ('你的成绩等级为B')
    elif y>=60:
        return ('你的成绩等级为C')
    else:
        return ('你的成绩等级为D')
print(judge(y))



3、
def f(p):
    l = []
    for i in range(len(p)):
        if i % 2 == 0:
            l.append(p[i])
    return l
nf = f([1,2,3,4,5,6,7])
print(nf)



4、 
n = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k ) and (j != k ):
                print(i*100+j*10+k)
                n += 1
print("一共有%s组" % n)



5、
x = int(input('请输入第一个数:'))
y = int(input('请输入第二个数:'))
z = int(input('请输入第三个数:'))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)



6、
n = eval(input('请输入n的值:'))
def qiuhe(n):
    sum = 0
    if n%2 != 0:
        for i in range(1,n+1,2):
            sum = sum + 1/i
    else:
        for i in range(2,n+1,2):
            sum = sum + 1/i
    return sum

print(qiuhe(n))